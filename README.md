# yolov4-deepsort
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HwclVZ9sl_lWjhdGWTJ-0SW6o7lRJWp0#scrollTo=nv5yDQptaJRE)

Le trafic automobile pose un problème de gestion majeur dans les sociétés africaines. A Dakar, le nombre d'automobiles augmente rapidement et les embouteillages deviennent de plus en plus fréquents. Disposer de moyens d’étude du trafic permettrait de trouver
plus facilement des solutions au problème.
Les systèmes de surveillance du trafic constituent un moyen de lutte contre la congestion du trafic. En effet, le suivi et le comptage précis des véhicules selon leurs catégories est d’une importance cruciale pour l'exploitation efficace du trafic, l'amélioration de la
sécurité et la planification des transports et également pour servir de données d’entrée pour les simulateurs du trafic.
Notre objectif  est de créer un outil informatique qui permet de détecter, compter le nombre de véhicules de chaque catégorie de transport au Sénégal présente sur une vidéo de surveillance. Par catégorie de transport, nous entendons les car rapide,
Ndiaga-Ndiaye, Dakar Dem Dikk (DDD), Tata, Moto et les voitures des particuliers.
Les véhicules comptés pourront servir de données d’entrée pour les simulateurs. Cet outil pourra également être intégrée à un système d’aide à la gestion du trafic (SAGT) par les structures comme la CETUD qui bénéficieront d’un ensemble d’informations décrivant
l’état de la circulation routière.
Notre solution est basée sur les avancées récentes de la vision par ordinateur avec les
techniques de Deep Learning.
Mise en œuvre avec YOLOv4, DeepSort et TensorFlow. YOLOv4 est un algorithme de pointe qui utilise des réseaux de neurones à convolution profonde pour effectuer des détections d'objets. Nous pouvons prendre la sortie de YOLOv4 pour alimenter ces détections d'objets dans Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) afin de créer un traqueur d'objets très précis.

## Démo Object Tracker sur les voitures
<p align="center"><img src="data/helpers/demo.gif"\></p>

## Getting Started
Pour commencer, installons les dépendances appropriées via Anaconda ou Pip. Je recommande l'itinéraire Anaconda pour les personnes utilisant un GPU car il configure la version de la boîte à outils CUDA pour nous.

### Conda (Recommendé)

```bash
# Tensorflow CPU
conda env create -f conda-cpu.yml
conda activate yolov4-cpu

# Tensorflow GPU
conda env create -f conda-gpu.yml
conda activate yolov4-gpu
```

### Pip
(TensorFlow 2 packages require a pip version >19.0.)
```bash
# TensorFlow CPU
pip install -r requirements.txt

# TensorFlow GPU
pip install -r requirements-gpu.txt
```
### Nvidia Driver (Pour le GPU, si nous n'utilisons pas l'environnement Conda et que nous n'avons pas encore configuré CUDA)

https://developer.nvidia.com/cuda-10.1-download-archive-update2

## Téléchargement officiel des poids pré-entraînés YOLOv4 
Notre traqueur d'objets utilise YOLOv4 pour effectuer les détections d'objets, que DeepSort utilise ensuite pour faire le suivi. Il existe un modèle officiel de détecteur d'objets YOLOv4 pré-entraîné capable de détecter 80 classes. Une fois notre modèle formé, on télelecharge le poids préformé yolov4.weights , on le copie de notre dossier de téléchargements et on le colle  dans le dossier 'data' de ce référentiel.

Nous pouvons utiliser yolov4-tiny.weights, un modèle plus petit qui exécute plus rapidement les détections mais moins précis, à télecharger ici : https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights

## Runnont tracker with YOLOv4
Pour implémenter le suivi d'objet à l'aide de YOLOv4, nous convertissons d'abord les .weights dans le modèle TensorFlow correspondant qui sera enregistré dans un dossier de points de contrôle. Ensuite, tout ce que nous avons à faire est d'exécuter le script object_tracker.py pour exécuter notre suivi d'objet avec YOLOv4, DeepSort et TensorFlow.

```bash
# Convertion des poidss darknet en modèle tensorflow
python save_model.py --model yolov4 

# Exécution du traqueur d'objets deepsort  en vidéo
python object_tracker.py --video ./data/video/video.mp4 --output ./outputs/video.mp4 --model yolov4

# Run yolov4 deep sort object tracker on webcam (set video flag to 0)
python object_tracker.py --video 0 --output ./outputs/webcam.avi --model yolov4
```
L'indicateur de sortie nous permet d'enregistrer la vidéo résultante du suivi d'objet en cours d'exécution afin que vous puissiez la revoir plus tard. La vidéo sera enregistrée dans le chemin que nous avons défini. (le dossier de sortie est là où il se trouvera si nous exécutons la commande ci-dessus !)


## Running the Tracker with YOLOv4-Tiny
Les commandes suivantes nous permettront d'exécuter le modèle yolov4-tiny. Yolov4-tiny nous permet d'obtenir une vitesse plus élevée (FPS) pour le tracker à un léger coût de précision. Assurons-nous d'avoir téléchargé le fichier de poids minuscules et de l'avoir ajouté au dossier "data" pour que les commandes fonctionnent !

```
# save yolov4-tiny model
python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --model yolov4 --tiny

# Run yolov4-tiny object tracker
python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ./data/video/test.mp4 --output ./outputs/tiny.avi --tiny
```

## Resulting Video
Comme mentionné ci-dessus, la vidéo résultante sera enregistrée là où nous définissons le chemin de l'indicateur de ligne de commande ``--output``. Je l'ai configuré pour enregistrer dans le dossier "outputs". Nous pouvons également modifier le type de vidéo enregistrée en ajustant le drapeau ``--output_format``, par défaut, il est défini sur le codec AVI qui est XVID.



## Command Line Args Reference

```bash
save_model.py:
  --weights: path to weights file
    (default: './data/yolov4.weights')
  --output: path to output
    (default: './checkpoints/yolov4-416')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --input_size: define input size of export model
    (default: 416)
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
    
 object_tracker.py:
  --video: path to input video (use 0 for webcam)
    (default: './data/video/test.mp4')
  --output: path to output video (remember to set right codec for given format. e.g. XVID for .avi)
    (default: None)
  --output_format: codec used in VideoWriter when saving video to file
    (default: 'XVID)
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'false')
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.50)
  --dont_show: dont show video output
    (default: False)
  --info: print detailed info about tracked objects
    (default: False)
```

### References  

   
Un grand bravo à hunglc007 et nwojke pour avoir créé les backbones de ce référentiel :
  * [tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite)
  * [Deep SORT Repository](https://github.com/nwojke/deep_sort)
