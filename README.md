# Staj-Dersi-
adam asmaca oyunu 
Bu proje, klasik Adam Asmaca oyununun Python ile geliştirilmiş basit bir konsol uygulamasıdır. Oyuncuların Türkçe kelimeleri tahmin ederek keyifli vakit geçirmesini sağlar.

Çözülen Sorunlar 
Türkçe karakter desteği (İ/i, I/ı dönüşümleri)
Konsol tabanlı basit bir oyun arayüzü
Oyun durumunun görsel olarak temsili (ASCII art)
Kelime tahmin mekaniklerinin dengelenmesi

Temel Özellikler
Dinamik Kelime Havuzu: 15+ Türkçe kelime içeren rastgele seçim
Görsel Geri Bildirim: 7 aşamalı asılma animasyonu
Akıllı Tahmin Yönetimi:
Harf ve kelime tahmin seçenekleri
Tekrarlanan harf koruması
Yanlış harflerin kaydı
Oyun Döngüsü Kontrolü:
Kazanma/kaybetme koşulları
Tekrar oynama seçeneği
Can sayacı (6 hata hakkı)

Temel Modüller/Teknolojiler:
Python kütüphaneleri kullanılarak yazılmıştır.
random: Kelimelerin rastgele seçimi
os: Konsol ekran temizleme (platform bağımsız)
String Manipülasyon: Türkçe karakter dönüşümleri
Dinamik Liste Yönetimi: Kelime haritalama ve durum takibi


Nasıl Oynanır?
Program rastgele bir kelime seçer
Oyuncu harf veya kelime tahmininde bulunur
Doğru harfler kelime üzerinde gösterilir
Yanlış tahminlerde:
Adam asmaca görseli bir etap ilerler
Yanlış harfler listelenir
Kalan tahmin hakkı azalır
Kelime tam tahmin edilirse oyunu kazanırsınız
6 yanlış tahminde adam asılır ve oyunu kaybedersiniz.
