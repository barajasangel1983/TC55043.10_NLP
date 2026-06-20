"""
Diagnóstico: verificar que los archivos descargados sean audio real,
no HTML corrupto o páginas web.
"""
import os
import struct
import wave

def check_file_type(filepath):
    """Verifica el tipo real de archivo por su magic bytes."""
    with open(filepath, 'rb') as f:
        header = f.read(512)
    
    info = []
    
    # Check MP3 (ID3 tags or sync frame)
    if header[:3] == b'ID3':
        info.append("✅ MP3 (con tag ID3)")
    elif header[:2] == b'\xff\xfb' or header[:2] == b'\xff\xfa' or header[:2] == b'\xff\xf3' or header[:2] == b'\xff\xf2':
        info.append("✅ MP3 (sync frame detectado)")
    
    # Check WAV
    if header[:4] == b'RIFF' and b'WAVE' in header:
        info.append("✅ WAV")
    
    # Check HTML
    if header[:20].lower().count(b'<!doctype') or header[:200].lower().count(b'<html'):
        info.append("❌ HTML (archivo web, NO es audio)")
    
    # Check UTF-8 text
    try:
        text = header.decode('utf-8', errors='strict')
        if any(word in text.lower() for word in ['suscríbete', 'canal', 'html', '<!doc']):
            info.append("❌ HTML/Texto (NO es audio)")
    except:
        pass
    
    # Check file size
    size = os.path.getsize(filepath)
    info.append(f"📦 Tamaño: {size:,} bytes ({size/1024:.1f} KB)")
    
    # Try to detect duration with ffprobe or librosa
    try:
        import librosa
        audio, sr = librosa.load(filepath, sr=None, duration=5)
        duration = len(audio) / sr
        info.append(f"🎵 Audio válido → duración detectada: {duration:.1f}s (sr={sr})")
    except Exception as e:
        info.append(f"❌ No es audio válido: {type(e).__name__}")
    
    return "\n".join(info)

# ── Verificar todos los archivos ──
FOLDER = "audios_esopo"
if not os.path.exists(FOLDER):
    print(f"⚠️ Folder '{FOLDER}' no existe. Descarga primero los audios.")
else:
    print("=" * 70)
    print("DIAGNÓSTICO DE ARCHIVOS")
    print("=" * 70)
    
    for fname in sorted(os.listdir(FOLDER)):
        fpath = os.path.join(FOLDER, fname)
        if os.path.isfile(fpath):
            print(f"\n📄 {fname}")
            print(check_file_type(fpath))
            print("-" * 70)
