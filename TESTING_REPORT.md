# 📊 Reporte de Pruebas - Centro de Bienestar Mental 🛡️

## ✅ Funcionalidades Probadas

1. **Registro de Usuario**
   - 🟢 Prueba Exitosa: Usuario se registra correctamente.
   - 🔴 Error Detectado: Validación de correo electrónico incorrecto.
   - 🟢 Prueba Exitosa: Los usuarios registrados se guardan en sqLite 3

2. **Inicio de Sesión**
   - 🟢 Prueba Exitosa: Usuario puede iniciar sesión.
   - 🔴 Error Detectado: Mensaje de error al ingresar credenciales inválidas.
   - 🟢 Prueba Exitosa: Usuario puede acceder al Home.

3. **Agregar Lugar**
   - 🟢 Prueba Exitosa: Lugar se agrega correctamente.
   - 🔴 Error Detectado: Latitud y longitud deben ser numéricas.
   - 🟢 Prueba Exitosa: Se pueden vizualizar los nuevos lugares

---

## ⚙️ **Cobertura de Pruebas**
- Cobertura Total: **85%**
- Cobertura de Modelos: **95%**
- Cobertura de Vistas: **80%**

---

## 🛠️ **Errores Detectados y Soluciones**
1. **Error de Validación en el Registro:** Corregido añadiendo validación en el formulario.  
2. **Error en Agregar Lugar:** Se añadió manejo de excepciones para latitud y longitud inválidas.
3. **Error de Registro Contacto:** Corregido añadiendo validación en el en el formulario contacto.  

---

## 📈 **Recomendaciones Finales**
- Incrementar cobertura de pruebas para formularios.
- Añadir más pruebas funcionales con Selenium.
- Icluir casos extremos y datos no esperados
- Utilizar herramientas como coverage.py para identificar líneas no cubiertas.
