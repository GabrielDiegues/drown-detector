# Grupo:
- Bernardo Pinto Rocha | RM: 99209
- Gabriel Diegues Figueiredo Rocha | RM: 550788
- Levy Nascimento Junior | RM: 98655

# 🌊 Drown Detector

**Drown Detector** é um sistema de visão computacional que utiliza `MediaPipe` e `OpenCV` para detectar **comportamentos de risco em situações de possível afogamento** através da análise de poses corporais em vídeos. A aplicação identifica sinais como posturas submersas, posições corporais suspeitas e pedidos de ajuda com os braços erguidos.

---

## 📌 Descrição do Problema

Afogamentos são um grande risco quando estamos falando de desastres como: enchentes e deslizamentos. Identificar sinais de perigo precocemente pode salvar vidas. Entretanto, em ambientes com múltiplas pessoas e distrações, sinais de afogamento podem passar despercebidos.

---

## 🎯 Objetivo da Solução

Drown Detector visa automatizar a **detecção precoce de possíveis afogamentos** por meio da análise em tempo real de vídeos (ou gravações) utilizando o modelo de pose do **MediaPipe**.

A aplicação reconhece:

* **Postura de risco**: nariz abaixo do quadril.
* **Submersão parcial**: quadril abaixo da linha d’água simulada.
* **Pedido de ajuda**: ambos os braços erguidos acima dos ombros.

Ao identificar um desses estados, o sistema exibe um alerta visual e salva um frame da detecção.

---

## ⚙️ Tecnologias Utilizadas

* [Python 3.10+](https://www.python.org/)
* [MediaPipe](https://google.github.io/mediapipe/)
* [OpenCV](https://opencv.org/)
* [Virtual Environment (venv)](https://docs.python.org/3/library/venv.html)

---

## 🧪 Ambiente Virtual (venv)

Para manter as dependências isoladas, o projeto utiliza um ambiente virtual localizado em `.venv`.

### 🔧 Passo a Passo para rodar o projeto:

#### 1. Clone o repositório

```bash
git clone https://github.com/GabrielDiegues/drown-detector.git
cd floodpose
```

#### 2. Ative o ambiente virtual

##### No **Windows**:

```bash
.venv\Scripts\activate
```

##### No **Linux / macOS**:

```bash
source .venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se ainda não existir, crie o `requirements.txt` com:
>
> ```
> opencv-python
> mediapipe
> ```

#### 4. Adicione seu vídeo de entrada

Coloque o arquivo do vídeo (ex: `afogamento1.mp4`) na raiz do projeto.

#### 5. Execute o script principal

```bash
python DrownDetector.py
```

---

## 🎥 Interface

* A janela exibirá o vídeo com as marcações da pose humana.
* Ao detectar um estado crítico, será exibido um alerta como:

  ```
  Alerta: submerso
  ```
* A imagem será salva com timestamp no formato `alerta_YYYYMMDD_HHMMSS_MICROS.jpg`.

---

## 📂 Estrutura de Arquivos

```
drown-detector/
│
├── afogamento1.mp4              # Vídeo de entrada
├── alerta_*.jpg                 # Imagens geradas com alerta
├── floodpose.py                 # Código principal
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo
```

---

## 🚨 Exemplos de Alertas

* `risco_postura`: quando o nariz está abaixo do quadril.
* `submerso`: quando a água (simulada) está baixa e o quadril está muito abaixo.
* `pedido_ajuda`: ambos os braços erguidos acima dos ombros.

---

## 📌 Observações

* A "altura da água" é simulada como a posição do joelho esquerdo, por simplicidade.
* O sistema pode ser adaptado para vídeos em tempo real com `cv2.VideoCapture(0)`.

---

## 📃 Licença

Este projeto é apenas para fins acadêmicos e experimentais.
