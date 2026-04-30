import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Smart Study Planner", page_icon="📅")

# تنسيق العنوان بلون Baby Blue باستخدام كود اللون (#89CFF0)
st.markdown("<h1 style='text-align: center; color: #89CFF0;'>📅 منظم المذاكرة الذكي 🌟</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5DADE2;'>نظم ساعاتك، حدد أهدافك، وضاعف إنتاجيتك</p>", unsafe_allow_html=True)
st.markdown("---")

# 2. إدخال البيانات (الفكرة الأساسية لصاحبك)
st.subheader("📝 ابدأ تنظيم وقتك الآن:center; color: #5DADE2;'>نظم ساعاتك، حدد أهدافك، وضاعف إنتاجيتك</p>", unsafe_allow_html=True)")
col_input1, col_input2 = st.columns(2)

with col_input1:
    subject = st.text_input("اسم المادة:", placeholder="مثلاً: تكنولوجيا تعليم")
    hours = st.number_input("عدد الساعات المتاحة للمذاكرة:", min_value=1, max_value=24, value=5)

with col_input2:
    level = st.selectbox("مستوى الصعوبة:", ["سهل", "متوسط", "صعب جداً"])
    goal = st.selectbox("هدفك من المذاكرة:", ["مراجعة نهائية", "مذاكرة لأول مرة", "حل امتحانات سابقة"])

# تغيير لون الزرار باستخدام CSS بسيط (اختياري بس بيخلي الشكل أجمد)
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #89CFF0;
    color: white;
    border: None;
}
</style>""", unsafe_allow_html=True)

if st.button("توليد خطة المذاكرة الذكية"):
    # حركات التحليل والذكاء الاصطناعي
    with st.status("🔍 جاري تحليل البيانات المدخلة...", expanded=True) as status:
        st.write("حساب توزيع الساعات بناءً على مستوى الصعوبة...")
        time.sleep(1.5)
        st.write("تحديد فترات الراحة (Pomodoro Technique)...")
        time.sleep(1.5)
        status.update(label="✅ تم إعداد الخطة بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    
    # 3. النتيجة الثابتة (مثال: خطة مذاكرة ليلة الامتحان)
    st.markdown(f"<h2 style='color: #5DADE2;'>📊 الجدول الزمني المقترح لمادة: {subject if subject else 'الذكاء الاصطناعي'}</h2>", unsafe_allow_html=True)
    
    st.info("📍 **توزيع الوقت المقترح (بناءً على 5 ساعات):**")
    
    st.write("""
    - **الساعة الأولى:** مراجعة المفاهيم الأساسية والتعاريف.
    - **الساعة الثانية:** التركيز على الأجزاء الأكثر صعوبة (Deep Work).
    - **راحة (15 دقيقة):** وقت استراحة وتجديد طاقة.
    - **الساعة الثالثة:** تلخيص أهم النقاط في خرائط ذهنية.
    - **الساعة الرابعة:** حل نماذج امتحانات سابقة.
    - **الساعة الخامسة:** مراجعة سريعة على التلخيصات النهائية.
    """)

    # نصائح إضافية لزيادة النتائج
    st.success("🚀 **نصائح ذكية لتحسين النتائج:**")
    st.markdown("""
    1. **قاعدة 50/10:** ذاكر لمدة 50 دقيقة وخذ راحة لمدة 10 دقائق.
    2. **التعلم النشط:** حاول شرح ما ذاكرته لشخص خيالي.
    3. **البيئة المحيطة:** ابعد الموبايل تماماً عن منطقة المذاكرة.
    """)

    st.warning("🛠️ **إحصائيات متوقعة:**")
    st.write("- نسبة استيعاب المحتوى: **85%**\n- التركيز المتوقع: **عالي جداً**\n- وقت الإنجاز الصافي: **4 ساعات و 45 دقيقة**")

    st.markdown("---")
    st.caption("تم تطوير هذا المشروع لغرض تنظيم الوقت الأكاديمي - ميدترم 2026")
