import cv2
import os
import numpy as np

# 1. Configurações Iniciais
img_path = 'buque.png'  # Nome do seu arquivo original
output_dir = 'assets_apresentacao_2'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

tamanho_alvo = 0

# 2. Carregar Original
img_bgr = cv2.imread(img_path)
if img_bgr is None:
    print(f"Erro: Não encontrei o arquivo {img_path}")
else:
    # Salvar canais RGB Originais (em tons de cinza para mostrar intensidade)
    b_orig, g_orig, r_orig = cv2.split(img_bgr)
    cv2.imwrite(f'{output_dir}/01_R_original.png', r_orig)
    cv2.imwrite(f'{output_dir}/02_G_original.png', g_orig)
    cv2.imwrite(f'{output_dir}/03_B_original.png', b_orig)

    # 3. Gerar a versão JPEG Comprimida (Qualidade 5 para evidenciar falhas)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 5]
    _, enc_img = cv2.imencode('.jpg', img_bgr, encode_param)
    tamanho_alvo = len(enc_img)
    img_jpg = cv2.imdecode(enc_img, 1)
    cv2.imwrite(f'{output_dir}/04_imagem_comprimida_final.jpg', img_jpg)

    # 4. Isolar Canais da Imagem Comprimida (RGB)
    b_jpg, g_jpg, r_jpg = cv2.split(img_jpg)
    cv2.imwrite(f'{output_dir}/05_R_comprimido.png', r_jpg)
    cv2.imwrite(f'{output_dir}/06_G_comprimido.png', g_jpg)
    cv2.imwrite(f'{output_dir}/07_B_comprimido.png', b_jpg)

    # 5. O segredo da CG: Canais YCbCr (Luminância e Crominância)
    img_ycbcr = cv2.cvtColor(img_jpg, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(img_ycbcr)
    
    cv2.imwrite(f'{output_dir}/08_Y_Luminancia (Nitidez).png', y)
    cv2.imwrite(f'{output_dir}/09_Cb_Crominancia (Cor_Azulada).png', cb)
    cv2.imwrite(f'{output_dir}/10_Cr_Crominancia (Cor_Avermelhada).png', cr)

print(f"Sucesso! 10 imagens foram salvas na pasta: {output_dir}")
