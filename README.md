# APF3-Detector-Wincha
# Detector de wincha con Haar Cascade (APF3)

**Autor:** Jean Piere Alair Bruno Silupu
**Curso:** Herramientas - Universidad Tecnológica del Perú
**Objeto seleccionado:** Wincha (cinta métrica)

## Descripción
Detector en tiempo real de una wincha usando OpenCV y un clasificador Haar Cascade
entrenado con un dataset propio. El sistema dibuja un rectángulo verde y la
etiqueta "Wincha" sobre el objeto detectado, usando DroidCam o webcam.

## Aplicación en Ingeniería Civil
Permite identificar herramientas de medición en obra, por ejemplo para el
control de inventario de herramientas o para verificar que el personal cuente
con sus equipos de medición.

## Estructura del repositorio
- `dataset.zip`: dataset propio (carpeta `p` con imágenes positivas y carpeta `n` con negativas)
- `Detector_Wincha_p.py`: captura de imágenes positivas
- `Detector_Wincha_n.py`: captura de imágenes negativas
- `cascade.xml`: modelo entrenado
- `APF3_NombreApellido.py`: detector en tiempo real
- `capturas/`: capturas del dataset y de los resultados

## Dataset
- 151 imágenes positivas (con la wincha) y 150 negativas (sin la wincha).
- Capturadas por mí con DroidCam, con variación de posición, fondo e iluminación.
- Tamaño de cada imagen: 38 píxeles de ancho.

## Entrenamiento
Se entrenó con Cascade Trainer GUI. Parámetros usados:
- Tamaño de muestra: 38 x 38
- Imágenes usadas: 151 positivas y 150 negativas
- Número de etapas: [NÚMERO]
- Tipo de características: [Haar o LBP]
- Archivo generado: cascade.xml

## Cómo ejecutar
1. Instalar dependencias: `pip install "opencv-python<5"`
2. Poner `cascade.xml` en la misma carpeta que el detector.
3. Cambiar la IP de DroidCam en el código por la de tu celular (o usar la webcam).
4. Ejecutar `APF3_NombreApellido.py`. Tecla ESC para salir.

## Resultados
- Pruebas realizadas: [20]
- Detecciones correctas: 14
- Falsos positivos: 6
- Falsos negativos: 5

## Limitaciones
funciona peor con poca luz, con ángulos distintos a los del dataset
o con fondos muy diferentes a los usados al entrenar.

## Posibles mejoras
más imágenes, más variedad de iluminación y fondos, más etapas de
entrenamiento.
