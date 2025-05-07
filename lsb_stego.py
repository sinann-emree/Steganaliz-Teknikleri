import wave

def encode_lsb(audio_path, message, output_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    message = message.ljust(160, '#')
    
    bits = ''.join([format(ord(i), '08b') for i in message])
    
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bit)
        
    modified_audio = wave.open(output_path, 'wb')
    modified_audio.setparams(audio.getparams())
    modified_audio.writeframes(bytes(frame_bytes))
    modified_audio.close()

def decode_lsb(audio_path):
    audio = wave.open(audio_path, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    extracted = [frame_bytes[i] & 1 for i in range(160 * 8)]
    message = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    return message.strip('#')

message = "Bu bir test mesajidir. Buraya kadar toplamda 160 karakterlik veri gömülebilir, kalanlar otomatik tamamlanr."
encode_lsb('input.wav', message, 'encoded.wav')

print("Gizli Mesaj:", decode_lsb('encoded.wav'))
