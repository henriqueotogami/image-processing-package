# Image Processing Package

> Pacote Python para processamento de imagens com funcionalidades de correspondência de histograma, similaridade estrutural e redimensionamento. Projeto desenvolvido no Bootcamp Developer Full Stack Python da Digital Innovation One.

## Autoria
- **Projeto original:** Karina Tiemi Kato (Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take)
- **Publicação no Test PyPI:** Henrique Matheus Alves Pereira
- **Aula:** Coding Lab PRO - Digital Innovation One
- [(clique aqui para ver o meu perfil na plataforma)](https://web.digitalinnovation.one/users/henrique_map)
- **Tecnologia:** Python
- **Data:** 22/08/2020

---

## 📋 Sobre o Projeto

Este pacote oferece ferramentas para processamento de imagens em Python, incluindo correspondência de histograma, cálculo de similaridade estrutural, redimensionamento e visualização. Foi criado como demonstração para publicação no Test PyPI durante o Bootcamp Developer Full Stack Python.

## 📁 Estrutura do Projeto

### Módulo Processing (`image_processing-test/processing/`)
- **combination.py** - Correspondência de histograma e similaridade estrutural entre imagens
- **transformation.py** - Redimensionamento de imagens por proporção

### Módulo Utils (`image_processing-test/utils/`)
- **io.py** - Leitura e gravação de imagens
- **plot.py** - Visualização de imagens, resultados e histogramas

## 📂 Estrutura do repositório

```
LICENSE
README.md
setup.py
requirements.txt
image_processing-test/
  __init__.py
  processing/
    combination.py    # correspondência de histograma e similaridade estrutural
    transformation.py # redimensionamento de imagens
  utils/
    io.py             # ler e salvar imagens
    plot.py           # plotar imagens, resultados e histogramas
```

## 🛠️ Tecnologias Utilizadas

- **Python** (>= 3.8) - Linguagem de programação
- **scikit-image** - Processamento de imagens (histograma, similaridade, resize)
- **NumPy** - Operações numéricas
- **matplotlib** - Visualização de imagens e gráficos

## 📝 Funcionalidades Principais

### Módulo Processing
- **Correspondência de histograma** - `transfer_histrogram(image1, image2)` - Ajusta o histograma de uma imagem ao de outra
- **Similaridade estrutural** - `find_difference(image1, image2)` - Calcula e retorna a diferença estrutural entre duas imagens
- **Redimensionar imagem** - `resize_image(image, proportion)` - Redimensiona imagem mantendo proporção (0 a 1)

### Módulo Utils
- **Ler imagem** - `read_image(path, is_gray)` - Carrega imagem do disco
- **Salvar imagem** - `save_image(image, path)` - Salva imagem no disco
- **Plotar imagem** - `plot_image(image)` - Exibe imagem
- **Resultado do gráfico** - `plot_result(*args)` - Exibe múltiplas imagens comparativas
- **Plotar histograma** - `plot_histogram(image)` - Exibe histograma RGB da imagem

## 🚀 Instalação

### Via Test PyPI (ambiente de testes)

```bash
pip install -i https://test.pypi.org/simple/ image-processing-test
```

### Dependências (instalação local)

```bash
pip install -r requirements.txt
```

## 📖 Como Usar

```python
from image_processing_test.processing import combination
from image_processing_test.processing import transformation
from image_processing_test.utils import io, plot

# Carregar imagens
image1 = io.read_image('imagem1.png')
image2 = io.read_image('imagem2.png')

# Encontrar diferença estrutural entre imagens
diff = combination.find_difference(image1, image2)
plot.plot_image(diff)

# Correspondência de histograma
matched = combination.transfer_histrogram(image1, image2)
plot.plot_image(matched)

# Redimensionar imagem
resized = transformation.resize_image(image1, proportion=0.5)
plot.plot_image(resized)
```

![Exemplo de processamento](https://github.com/henriqueotogami/image-processing-package/blob/master/image-processing-test.png?raw=true)

## ⚙️ Como funciona

### Similaridade Estrutural
A função `find_difference` implementa o seguinte algoritmo:
1. Converte as imagens para escala de cinza
2. Calcula o índice de similaridade estrutural (SSIM) entre as duas imagens
3. Normaliza a imagem de diferença para exibição
4. Retorna a imagem de diferença e exibe o score de similaridade

### Correspondência de Histograma
A função `transfer_histrogram` usa `match_histograms` do scikit-image para ajustar o histograma de cores da primeira imagem ao da segunda, permitindo transferência de estilo ou equalização entre imagens.

---

## 📦 Publicação no Test PyPI

### Passo a passo para hospedar o pacote

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```bash
py -m pip install --user --upgrade setuptools wheel
```

- [x] Gerar distribuição (certifique-se de estar no diretório do projeto)

```bash
py setup.py sdist bdist_wheel
```

- [x] Verificar se as pastas foram criadas:
  - build
  - dist
  - image_processing_test.egg-info

- [x] Upload para o Test PyPI via Twine

```bash
py -m twine upload --repository testpypi dist/*
```

**Nota:** O Test PyPI é um ambiente de testes. Para disponibilizar publicamente, publique no [PyPI oficial](https://pypi.org/).

---

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📖 Referências

- [Digital Innovation One](https://web.digitalinnovation.one/)
- [scikit-image Documentation](https://scikit-image.org/)
- [Test PyPI](https://test.pypi.org/)
- [PyPI](https://pypi.org/)

---

### Hashtags
#Python #ImageProcessing #OpenSource #DataScience #MachineLearning #DigitalInnovationOne #Bootcamp #PyPI #scikit-image

### Meta Keywords
```
processamento de imagens, Python, histograma, similaridade estrutural,
scikit-image, Digital Innovation One, PyPI, pacote Python, redimensionamento,
visualização de imagens, bootcamp, machine learning, data science
```
