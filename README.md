# YTU Yıldız Rover - Destek Ekip Ödev 3
**Derin Öğrenme ve Nesne Tespit Modelleri ile Trafik İşareti (STOP) Tespiti**

Bu repository, Yıldız Rover takımı 3. destek ödevi kapsamında geliştirilen, derin öğrenme tabanlı (YOLOv8) bir nesne tespit projesini içermektedir. Projenin amacı, otonom sistemler için geleneksel renk tespiti algoritmalarının yetersiz kaldığı durumlarda yapay zeka kullanarak yüksek doğrulukla "STOP" (Dur) tabelası tespiti yapmaktır.

## 📂 Proje Dosya Yapısı ve İçerikler

* `train.py`: Roboflow üzerinden veri setini indiren ve YOLOv8 Nano modelinin eğitimini (training) başlatan ana betiktir.
* `test.py`: Eğitilmiş olan en iyi model ağırlıklarını (`best.pt`) kullanarak, özel test veri seti (stop_sign_dataset) üzerinde tahmin (inference) yapan betiktir.
* `test_gpu.py`: PyTorch ortamının NVIDIA CUDA çekirdeklerini (GPU) görüp görmediğini test etmek ve donanım hızlandırmasını doğrulamak amacıyla yazılmış kontrol betiğidir.
* `runs/`: Eğitim boyunca elde edilen grafiklerin (Loss, mAP, Recall), test sonuçlarının ve modelin en iyi ağırlıklarının (`weights/best.pt`) kaydedildiği klasördür.
* `STOP-SIGN-1/`: Modelin eğitilmesi için kullanılan veri setidir (Train, Valid, Test olarak ayrılmıştır).

## ⚙️ Kurulum ve Gereksinimler

Projeyi kendi yerel bilgisayarınızda (local) çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install ultralytics roboflow torch torchvision torchaudio


## 🚀 Çalıştırma Talimatları

Bu bölüm, projenin yerel ortamda nasıl kurulacağını ve çalıştırılacağını adım adım açıklamaktadır.

### 1. Donanım Kontrolü (GPU Testi)
Eğitim ve test işlemlerinden önce, sisteminizdeki NVIDIA ekran kartının (GPU) ve CUDA desteğinin Python tarafından algılanıp algılanmadığını kontrol etmek için hazırladığım betiği çalıştırabilirsiniz:
python test_gpu.py


*(Bu dosya, donanım hızlandırmasının aktif olup olmadığını doğrular.)*

### 2. Modelin Eğitilmesi (Training)
Veri setini indirmek ve YOLOv8 modelini eğitmek için `train.py` dosyasını çalıştırınız:
python train.py
VRAM sınırlarının aşılmaması için batch 4 olarak ayarlanmıştır.

### 3. Test ve Tahmin (Inference)
Eğitilen modeli ödev kapsamında paylaşılan özel `stop_sign_dataset` klasörü üzerinde test etmek için `test.py` dosyasını çalıştırınız:
python test.py