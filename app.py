import streamlit as st
import pandas as pd
from core.charts import (
    plot_required_for_job,
    plot_level_hist,
    plot_requirement_scatter,
    plot_avg_level_by_skill,
)

# إعداد الصفحة لتكون واسعة واحترافية
st.set_page_config(
    page_title="UniGap Project",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تحسينات CSS لضبط الاتجاه العربي والأزرار والبطاقات
st.markdown("""
    <style>
    .rtl-box {
        direction: rtl;
        text-align: right;
        padding: 20px;
        border-radius: 12px;
        background-color: #1e293b;
        border: 1px solid #334155;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .rtl-text {
        direction: rtl;
        text-align: right;
    }
    div.stButton > button {
        direction: rtl;
        text-align: center;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# الشريط الجانبي (Sidebar)
st.sidebar.image("https://img.icons8.com/color/96/graduation-cap.png", width=80)
st.sidebar.title("UniGap Dashboard")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigate Sections",
    ["📊 Overview & Charts", "🎯 Gap Analysis & Path", "🤖 AI Career Assistant"]
)

st.sidebar.markdown("---")
st.sidebar.info("Developed by: UniGap Team\nProgramming Project")

# ==========================================
# القسم الأول: النظرة العامة والرسوم البيانية
# ==========================================
if page == "📊 Overview & Charts":
    st.title("🎓 UniGap — Skills Gap Analysis & Learning Recommendations")
    st.markdown("<p class='rtl-text' style='font-size: 16px; color: #94a3b8;'>لوحة تحكم ذكية لتحليل الفجوات المهارية للمتعلمين ومطابقتها مع متطلبات سوق العمل لتحديد المسارات التعليمية بدقة.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Task 1: ملخص المستويات
    st.subheader("1. 📈 Learner Skill Levels Summary")
    try:
        levels = pd.read_csv("output/learner_skills_cleaned.csv")
        req = pd.read_csv("data/job_requirements.csv")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Records", len(levels), delta="Cleaned Data")
        c2.metric("Total Learners", levels["learner_id"].nunique(), delta="Active")
        c3.metric("Tracked Skills", levels["skill_id"].nunique(), delta="Core")
        c4.metric("Average Level", round(float(levels["level"].mean()), 1), delta="Overall")
        
        with st.expander("🔍 Click to view raw learner data table"):
            st.dataframe(levels.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading files for Task 1: {e}")

    st.markdown("---")

    # Task 2: الرسوم البيانية المتوازنة
    st.subheader("2. 📊 Visualizations & Analytics")
    try:
        col1, col2 = st.columns(2)
        with col1:
            st.image(plot_level_hist(levels, "output/charts/unigap_level_hist.png"), use_container_width=True)
        with col2:
            st.image(plot_avg_level_by_skill(levels, "output/charts/unigap_avg_level.png"), use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c_left, c_mid, c_right = st.columns([1, 4, 1])
        with c_mid:
            st.image(plot_requirement_scatter(req, "output/charts/unigap_requirement_scatter.png"), use_container_width=True)
            
    except Exception as e:
        st.warning(f"Charts could not be loaded: {e}")

    st.markdown("---")
    with st.expander("⚙️ Methodology: How UniGap Calculates Skill Gaps"):
        st.markdown("""
        <div class='rtl-text'>
        <ul>
            <li><b>تنظيف البيانات (Data Cleaning):</b> معالجة القيم المفقودة وتوحيد معرفات المتعلمين والمهارات.</li>
            <li><b>حساب الفجوة (Gap Calculation):</b> يتم طرح مستوى المتعلم الحالي من المستوى المطلوب للوظيفة المستهدفة: <code>Gap = max(0, Required_Level - Current_Level)</code>.</li>
            <li><b>التوصية الذكية (Smart Recommendation):</b> ترشيح الدورات التدريبية المرتبطة حصرياً بالمهارات التي سجلت فجوة أكبر من الصفر.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# القسم الثاني: تحليل الفجوات والمسار التدريبي
# ==========================================
elif page == "🎯 Gap Analysis & Path":
    st.title("🎯 Target Job & Gap Analysis")
    st.markdown("<p class='rtl-text' style='font-size: 16px; color: #94a3b8;'>اختر المتعلم والوظيفة المستهدفة لمقارنة المهارات، قياس الفجوات، واستخراج خطة الدورات التدريبية فوراً.</p>", unsafe_allow_html=True)
    st.markdown("---")

    try:
        levels = pd.read_csv("output/learner_skills_cleaned.csv")
        req = pd.read_csv("data/job_requirements.csv")
        skills = pd.read_csv("data/skills.csv")
        jobs = pd.read_csv("data/jobs.csv")
        courses = pd.read_csv("data/courses.csv")

        skill_name_map = dict(zip(skills["skill_id"], skills["skill_name"]))

        # صف علوي موحد للقوائم المنسدلة لمنع أي فراغات جانبية
        st.subheader("⚙️ Analysis Controls")
        ctrl1, ctrl2, ctrl3 = st.columns(3)
        with ctrl1:
            selected_job_chart = st.selectbox("1. Preview Job Requirements", req["job_id"].unique())
        with ctrl2:
            learner = st.selectbox("2. Select Learner ID", levels["learner_id"].unique())
        with ctrl3:
            target = st.selectbox("3. Select Target Job ID", jobs["job_id"].unique())

        # دالة حساب الفجوات مع إضافة اسم المهارة
        def skill_gaps(levels_df, req_df, l_id, j_id):
            l_skills = levels_df[levels_df["learner_id"] == l_id].set_index("skill_id")["level"].to_dict()
            j_req = req_df[req_df["job_id"] == j_id].set_index("skill_id")["required_level"].to_dict()
            
            data = []
            for s_id, req_lvl in j_req.items():
                curr_lvl = l_skills.get(s_id, 0)
                gap = max(0, req_lvl - curr_lvl)
                data.append({
                    "Skill ID": s_id,
                    "Skill Name": skill_name_map.get(s_id, s_id),
                    "Required Level": req_lvl,
                    "Current Level": curr_lvl,
                    "Gap": gap
                })
            return pd.DataFrame(data)

        gaps = skill_gaps(levels, req, learner, target)

        def recommend_courses(gaps_df, courses_df):
            needed_skills = gaps_df[gaps_df["Gap"] > 0]["Skill ID"].tolist()
            return courses_df[courses_df["skill_id"].isin(needed_skills)]

        rec_courses = recommend_courses(gaps, courses)

        # مؤشرات الأداء الرئيسية (KPIs) لتحليل الفجوة
        st.markdown("---")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        total_gap = int(gaps["Gap"].sum())
        skills_needed = int((gaps["Gap"] > 0).sum())
        top_gap_skill = gaps.loc[gaps["Gap"].idxmax(), "Skill Name"] if total_gap > 0 else "None"

        kpi1.metric("⚠️ Total Gap Score", total_gap)
        kpi2.metric("📌 Skills to Improve", f"{skills_needed} / {len(gaps)}")
        kpi3.metric("🔥 Highest Priority Skill", top_gap_skill)
        kpi4.metric("📚 Recommended Courses", len(rec_courses))

        st.markdown("---")

        # توزيع متوازن 50% / 50% للرسم البياني والجدول
        col_left, col_right = st.columns(2)
        with col_left:
            st.markdown(f"**📊 Required Skill Levels for Job ({selected_job_chart})**")
            st.image(plot_required_for_job(req, selected_job_chart, f"output/charts/unigap_required_for_job_{selected_job_chart}.png"), use_container_width=True)

        with col_right:
            st.markdown(f"**📋 Gap Breakdown: Learner ({learner}) vs Job ({target})**")
            st.dataframe(gaps, use_container_width=True, height=340)

        st.markdown("---")

        # الرسم البياني التفاعلي للفجوات والدورات المقترحة جنباً إلى جنب
        b_left, b_right = st.columns(2)
        with b_left:
            st.subheader("📉 Skill Gap Distribution")
            st.bar_chart(gaps.set_index("Skill Name")["Gap"])

        with b_right:
            st.subheader("🎓 Recommended Learning Path")
            if not rec_courses.empty:
                st.dataframe(rec_courses, use_container_width=True)
                st.download_button(
                    label="📥 Download Learning Plan (CSV)",
                    data=rec_courses.to_csv(index=False),
                    file_name=f"UniGap_Path_{learner}_{target}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.success("🎉 Great news! This learner meets all requirements for the target job.")
            
    except Exception as e:
        st.error(f"Module 4 files check error: {e}")

# ==========================================
# القسم الثالث: المساعد الذكي (اتجاه RTL مضبوط)
# ==========================================
else:
    st.title("🤖 UniGap AI Career Assistant")
    st.markdown("<p class='rtl-text' style='font-size: 16px; color: #94a3b8;'>مساعد ذكي تفاعلي للاستشارات المهنية وتحليل فجوات المهارات. اختر أحد الأسئلة أدناه لعرض الاستشارة فوراً:</p>", unsafe_allow_html=True)
    st.markdown("---")

    if "ai_question" not in st.session_state:
        st.session_state.ai_question = "أهلاً بك في مساعد UniGap الذكي! يرجى اختيار أحد الأسئلة أدناه للاستعراض."
        st.session_state.ai_answer = "نحن هنا لمساعدتك في تحليل الفجوات المهارية وتحديد المسار التدريبي الأنسب لسوق العمل."

    # صندوق عرض احترافي مضبوط الاتجاه RTL بالكامل
    st.markdown(
        f"""
        <div class='rtl-box'>
            <p style='color: #94a3b8; font-size: 14px; margin-bottom: 6px;'><b>السؤال المحدد:</b></p>
            <p style='color: #f8fafc; font-size: 18px; font-weight: bold; margin-bottom: 16px;'>{st.session_state.ai_question}</p>
            <hr style='border-color: #334155; margin-bottom: 16px;'>
            <p style='color: #94a3b8; font-size: 14px; margin-bottom: 6px;'><b>الرد الاستشاري:</b></p>
            <p style='color: #38bdf8; font-size: 17px; line-height: 1.7; margin: 0;'>{st.session_state.ai_answer}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h4 class='rtl-text'>💡 اختر سؤالاً للاستعراض السريع:</h4>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    if c1.button("كيف أغطي الفجوة في مهارات بايثون (SK01)؟ 🔍", use_container_width=True):
        st.session_state.ai_question = "كيف أغطي الفجوة في مهارات بايثون (SK01)؟"
        st.session_state.ai_answer = "بناءً على تحليل الفجوات، تتطلب مهارة Python (SK01) رفع المستوى لتتوافق مع متطلبات الوظائف التقنية. نوصي بالتسجيل في دورة Advanced Python (C01) لرفع الكفاءة إلى 90."
        st.rerun()

    if c2.button("ما هي الدورات المقترحة لتطوير المسار المهني؟ 📚", use_container_width=True):
        st.session_state.ai_question = "ما هي الدورات المقترحة لتطوير المسار المهني؟"
        st.session_state.ai_answer = "يمكنك استعراض جدول الدورات المخصص لكل متعلم في قسم (Gap Analysis & Path)، كما يتيح النظام تحميل خطة التعلم بصيغة CSV بضغطة زر واحدة."
        st.rerun()

    if c3.button("كيف يفيد نظام UniGap المتعلمين وسوق العمل؟ 🎯", use_container_width=True):
        st.session_state.ai_question = "كيف يفيد نظام UniGap المتعلمين وسوق العمل؟"
        st.session_state.ai_answer = "يعمل النظام كجسر ذكي يطابق المهارات الفعلية للمتعلمين مع الاحتياجات الحقيقية للوظائف المستهدفة، مما يقلل الفجوة المعرفية ويوجه التدريب نحو المهارات الأكثر طلباً."
        st.rerun()

    if c4.button("كيف يتم حساب نقاط الفجوة المهارية بدقة؟ 📊", use_container_width=True):
        st.session_state.ai_question = "كيف يتم حساب نقاط الفجوة المهارية بدقة؟"
        st.session_state.ai_answer = "تُحسب الفجوة بطرح مستوى المتعلم الحالي من المستوى المطلوب للوظيفة (بحد أدنى 0)، وتُعامل المهارات غير المكتسبة بمستوى 0 افتراضياً لضمان شمولية ودقة التقييم."
        st.rerun()
