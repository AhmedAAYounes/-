import streamlit as st
import time

# 1. إعدادات واجهة الموقع
st.set_page_config(page_title="Smart Study Planner", page_icon="📅")

# --- كود تغيير الألوان لـ Baby Blue ---
st.markdown("""
    <style>
    /* تغيير لون العنوان الرئيسي */
    .main-title {
        color: #89CFF0 !important;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    /* تغيير لون الزرار */
    div.stButton > button:first-child {
        background-color: #89CFF0 !important;
        color: white !important;
        border: none;
        width: 100%;
    }
    /* تغيير لون العناوين الفرعية */
    h2, h3 {
        color: #5DADE2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. عرض العناوين بالستايل الجديد
st.markdown('<p class="main-title">📅 منظم المذاكرة الذكي 🌟</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5DADE2;'>نظم ساعاتك، حدد أهدافك، وضاعف إنتاجيتك</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. إدخال البيانات
st.subheader("📝 ابدأ تنظيم وقتك الآن:")
col_input1, col_input2 = st.columns(2)

with col_input1:
    subject = st.text_input("اسم المادة:", placeholder="مثلاً: تكنولوجيا تعليم")
    hours = st.number_input("عدد الساعات المتاحة للمذاكرة:", min_value=1, max_value=24, value=5)

with col_input2:
    level = st.selectbox("مستوى الصعوبة:", ["سهل", "متوسط", "صعب جداً"])
    goal = st.selectbox("هدفك من المذاكرة:", ["مراجعة نهائية", "مذاكرة لأول مرة", "حل امتحانات سابقة"])

if st.button("توليد خطة المذاكرة الذكية"):
    with st.status("🔍 جاري تحليل البيانات المدخلة...", expanded=True) as status:
        st.write("حساب توزيع الساعات...")
        time.sleep(1.5)
        status.update(label="✅ تم إعداد الخطة بنجاح!", state="complete", expanded=False)

    st.markdown("---")
    
    # النتيجة
    st.markdown(f"<h2 style='color: #89CFF0;'>📊 الجدول الزمني المقترح لمادة: {subject if subject else 'الذكاء الاصطناعي'}</h2>", unsafe_allow_html=True)
    
    st.info("📍 **توزيع الوقت المقترح (بناءً على 5 ساعات):**")
    st.write("""
    - **الساعة الأولى:** مراجعة المفاهيم الأساسية.
    - **الساعة الثانية:** التركيز على الأجزاء الصعبة.
    - **راحة (15 دقيقة).**
    - **الساعة الثالثة:** عمل خرائط ذهنية.
    - **الساعة الرابعة:** حل امتحانات سابقة.
    - **الساعة الخامسة:** مراجعة نهائية.
    """)

    st.success("🚀 **نصائح ذكية:**")
    st.markdown("1. قاعدة 50/10.\n2. التعلم النشط.\n3. ابعد الموبايل.")

    st.markdown("---")
    st.caption("تم تطوير هذا المشروع لغرض تنظيم الوقت الأكاديمي - ميدترم 2026")
