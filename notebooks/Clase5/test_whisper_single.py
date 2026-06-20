"""
Verificación rápida: reproducir un audio + transcribirlo con Whisper
y validar que el sample rate sea 16kHz.
"""
import librosa
import torch
from transformers import pipeline, AutoProcessor, AutoModelForSpeechSeq2Seq
import os
import re

# ── CONFIGURACIÓN ──
AUDIO_FILE = r"D:\ML\Projects\Project_6_TC55043.10_NLP\TC55043.10_NLP\data\Clase5\audios_esopo\21144-01.mp3"  # ← Ajusta si es diferente

# ── 1. Verificar el audio ──
print("=" * 60)
print("VERIFICACIÓN DE AUDIO")
print("=" * 60)

# Info del archivo
size = os.path.getsize(AUDIO_FILE)
print(f"Archivo: {AUDIO_FILE}")
print(f"Tamaño: {size / 1024 / 1024:.2f} MB")

# Cargar con sr=16000 (lo que Whisper espera)
audio, sr = librosa.load(AUDIO_FILE, sr=16000)
print(f"Sample rate: {sr} Hz")
print(f"Duración: {len(audio) / sr:.2f} segundos")
print(f"Muestras: {len(audio)}")
print(f"Rango de amplitud: [{audio.min():.3f}, {audio.max():.3f}]")

# Si sr != 16000, librosa hizo resampleo automático → OK
if sr != 16000:
    print(f"⚠️ Nota: librosa resampleó a {sr} Hz (no 16000)")

# ── 2. Probar Whisper ──
print("\n" + "=" * 60)
print("TRANSCRIPCIÓN CON WHISPER")
print("=" * 60)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Dispositivo: {device}")

model_id = "openai/whisper-large-v3-turbo"
print(f"Modelo: {model_id}")

print("\nCargando modelo... (esto puede tardar)")

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch.float32, low_cpu_mem_usage=True
).to(device)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch.float32,
    device=device,
)

# ── 3. Transcribir ──
print(f"\nTranscribiendo {os.path.basename(AUDIO_FILE)}...")
result = pipe(
    audio,
    return_timestamps=True,
    generate_kwargs={"language": "es"}
)

transcript = result["text"]
print(f"\n📝 Transcripción completa:")
print(transcript)
print(f"\nLongitud: {len(transcript)} caracteres")

# ── 4. Limpieza básica ──
intro_pattern = re.compile(r"las\s+fábulas\s+de\s+esopo.*?fábula\s+número\s+\d+", re.IGNORECASE)
cierre_pattern = re.compile(r"fin\s+de\s+la\s+fábula.*", re.IGNORECASE)

cleaned = intro_pattern.sub("", transcript).strip()
cleaned = cierre_pattern.sub("", cleaned).strip()
cleaned = re.sub(r"\s+", " ", cleaned)

print(f"\n📝 Después de limpieza:")
print(cleaned if cleaned else "(vacío)")
print(f"Longitud después de limpieza: {len(cleaned)} caracteres")

# ── 5. Verificación de calidad ──
print("\n" + "=" * 60)
print("VERIFICACIÓN DE CALIDAD")
print("=" * 60)

# Si el transcript es corto (< 50 chars), probablemente falló
if len(cleaned) < 50:
    print("⚠️ ALERTA: La transcripción es muy corta.")
    print("   Posibles causas:")
    print("   - El audio no es claro (calidad baja)")
    print("   - El audio es otro archivo (no de Esopo)")
    print("   - Problema de sample rate")
else:
    print("✅ Transcripción parece razonable")
    # Mostrar primeras 200 chars
    print(f"\nVista previa: {cleaned[:200]}...")
