# ============================================================
# 🎓 YuanZe IEM 教育版：專題教授推薦系統 (v5.7 圖文完美剝離版)
# ============================================================
import os
import urllib.parse
import matplotlib.pyplot as plt
import gradio as gr
import traceback

print("⏳ [1/2] 正在載入教授資料庫與問卷...")

professors_info = {
    "蔡介元": {"field": "AI、大數據分析、資料探勘", "intro": "適合喜歡人工智慧、機器學習與資料分析的學生。"},
    "呂卓勲": {"field": "資訊系統、網站開發、電子商務", "intro": "適合喜歡程式設計、系統開發與網站建置的學生。"},
    "蔡啟揚": {"field": "生產管理、供應鏈、智慧製造", "intro": "適合對企業流程改善與生產管理有興趣的學生。"},
    "潘劍輝": {"field": "作業研究、最佳化、決策分析", "intro": "適合喜歡數學建模與最佳化問題求解的學生。"},
    "林瑞豐": {"field": "人機互動、智慧醫療、使用者研究", "intro": "適合關心使用者需求與互動體驗的學生。"},
    "周金枚": {"field": "人因工程、產品設計、UX設計", "intro": "適合具有設計思維與創意發想能力的學生。"}
}

professors_reqs = {
    "蔡介元": {"course": "Python 程式設計、統計學、機器學習導論", "skill": "邏輯分析能力、數據處理思維"},
    "呂卓勲": {"course": "資料結構、網頁程式設計、資料庫系統", "skill": "系統架構規劃、前後端開發實作"},
    "蔡啟揚": {"course": "生產與作業管理、供應鏈管理、品質管理", "skill": "流程優化邏輯、系統化思考"},
    "潘劍輝": {"course": "作業研究、線性代數、微積分", "skill": "數學建模能力、最佳化演算法設計"},
    "林瑞豐": {"course": "人機互動概論、心理學、研究方法", "skill": "使用者需求分析、易用性測試評估"},
    "周金枚": {"course": "人因工程、產品設計、基礎繪圖軟體", "skill": "設計美感思維、創意發想與動手做"}
}

professors_photos = {
    "蔡介元": f"https://ui-avatars.com/api/?name={urllib.parse.quote('蔡介元')}&background=000000&color=fff&size=200&bold=true",
    "呂卓勲": f"https://ui-avatars.com/api/?name={urllib.parse.quote('呂卓勲')}&background=000000&color=fff&size=200&bold=true",
    "蔡啟揚": f"https://ui-avatars.com/api/?name={urllib.parse.quote('蔡啟揚')}&background=000000&color=fff&size=200&bold=true",
    "潘劍輝": f"https://ui-avatars.com/api/?name={urllib.parse.quote('潘劍輝')}&background=000000&color=fff&size=200&bold=true",
    "林瑞豐": f"https://ui-avatars.com/api/?name={urllib.parse.quote('林瑞豐')}&background=000000&color=fff&size=200&bold=true",
    "周金枚": f"https://ui-avatars.com/api/?name={urllib.parse.quote('周金枚')}&background=000000&color=fff&size=200&bold=true"
}

professors_papers = {
    "蔡介元": ["應用大數據分析於股市技術指標預測之研究", "基於機器學習之半導體產品良率預測模型", "AI影像辨識在產品瑕疵檢測之應用", "深度學習於智慧醫療影像病徵分類之研究"],
    "呂卓勲": ["結合RTSP影像串流之遠端監控系統架構設計", "電子商務平台之個人化推薦系統開發", "基於雲端架構之企業資源規劃系統整合", "智慧校園行動化導覽APP之設計與實作"],
    "蔡啟揚": ["應用程序分析(Process Mapping)改善餐飲業出餐流程", "智慧工廠之生產線佈置與動線最佳化設計", "應用精實生產降低製造現場之七大浪費", "自動化倉儲系統之儲位規劃與揀貨路徑優化"],
    "潘劍輝": ["考量多目標之供應鏈存貨最佳化數學模型", "物流配送路線規劃之啟發式演算法求解", "最佳化排程於半導體封裝廠之應用研究", "動態定價策略之賽局理論與最佳化分析"],
    "林瑞豐": ["結合藍牙與UHF通訊之智慧穿戴裝置介面評估", "高齡者智慧照護系統之使用者體驗研究", "行動醫療APP介面之易用性測試與改善", "虛擬實境(VR)遊戲介面設計與防暈眩機制探討"],
    "周金枚": ["手持式工具之應用人因工程設計與改良", "視覺化看板對作業員疲勞度影響之研究", "辦公室人體工學椅之舒適度評估與改良設計", "高齡者輔具產品之感性工程設計"]
}

questions = [
    {"q": "Q1 如果要做一學期的專題，你最想做哪一種？", "options": {"設計讓產品變得更方便使用": "周金枚", "研究如何讓公司運作得更有效率": "蔡啟揚", "開發網站或APP系統": "呂卓勲", "研究AI或分析大量資料": "蔡介元", "研究人們如何使用科技產品": "林瑞豐", "利用數學方法找出最佳解決方案": "潘劍輝"}},
    {"q": "Q2 看到新的科技新聞時，你最容易被什麼主題吸引？", "options": {"工廠自動化與智慧製造": "蔡啟揚", "人工智慧與機器學習": "蔡介元", "醫療科技與智慧照護": "林瑞豐", "電子商務與數位服務": "呂卓勲", "產品設計與使用體驗": "周金枚", "演算法與最佳化技術": "潘劍輝"}},
    {"q": "Q3 做報告時，你通常最喜歡負責什麼工作？", "options": {"蒐集數據並分析結果": "蔡介元", "設計產品外觀或介面": "周金枚", "規劃工作流程與時程": "蔡啟揚", "建立網站或系統功能": "呂卓勲", "研究使用者的想法與需求": "林瑞豐", "設計計算模型解決問題": "潘劍輝"}},
    {"q": "Q4 如果未來要選修一門課，你最想修哪一門？", "options": {"資料分析與AI應用": "蔡介元", "人機互動與智慧醫療": "林瑞豐", "生產管理與供應鏈": "蔡啟揚", "網頁系統開發": "呂卓勲", "作業研究與最佳化": "潘劍輝", "人因工程與產品設計": "周金枚"}},
    {"q": "Q5 你認為自己最大的優勢是？", "options": {"能快速理解程式與系統架構": "呂卓勲", "很會觀察別人的需求": "林瑞豐", "邏輯分析能力強": "潘劍輝", "喜歡改善流程與管理事情": "蔡啟揚", "對設計和美感很敏銳": "周金枚", "喜歡研究資料中的規律": "蔡介元"}},
    {"q": "Q6 下列哪個專題題目最吸引你？", "options": {"APP使用體驗改善研究": "林瑞豐", "AI預測模型建立": "蔡介元", "最佳送貨路線規劃": "潘劍輝", "智慧工廠排程改善": "蔡啟揚", "電商平台功能開發": "呂卓勲", "高齡者產品設計研究": "周金枚"}},
    {"q": "Q7 畢業後你最想從事哪種工作？", "options": {"資料分析師或AI工程師": "蔡介元", "產品設計師或UX設計師": "周金枚", "軟體工程師": "呂卓勲", "營運管理人員": "蔡啟揚", "使用者研究員": "林瑞豐", "決策分析師": "潘劍輝"}},
    {"q": "Q8 如果參加比賽，你最想挑戰哪一類？", "options": {"創新設計競賽": "周金枚", "商業流程改善競賽": "蔡啟揚", "程式設計競賽": "呂卓勲", "AI應用競賽": "蔡介元", "智慧醫療創新競賽": "林瑞豐", "數學建模競賽": "潘劍輝"}},
    {"q": "Q9 空閒時間學習新東西時，你最可能選擇？", "options": {"AI工具與資料分析": "蔡介元", "網頁或APP開發": "呂卓勲", "流程管理與企業經營": "蔡啟揚", "心理學與使用者行為": "林瑞豐", "最佳化演算法": "潘劍輝", "設計軟體與創意課程": "周金枚"}},
    {"q": "Q10 你最希望專題成果能達成什麼？", "options": {"幫助企業提升效率": "蔡啟揚", "開發一套能實際使用的系統": "呂卓勲", "找到資料背後的重要發現": "蔡介元", "提出最有效率的解決方案": "潘劍輝", "讓使用者有更好的體驗": "林瑞豐", "設計出更符合需求的產品": "周金枚"}}
]

def analyze_results(*answers):
    try:
        if not all(answers):
            warning_box = "<div style='background-color: #111; color: #fff; padding: 20px; border-radius: 12px; text-align: center; font-weight: 900; font-size: 18px; margin-bottom: 20px; border: 2px solid #ff4444;'>⚠️ 系統提示：您還有題目尚未作答完畢！請確認 10 題皆已選取後再送出。</div>"
            return (
                gr.update(visible=True, value=warning_box), 
                gr.update(visible=True), gr.update(visible=False), 
                gr.update(value=""), gr.update(value=None), gr.update(value=""), gr.update(value="")
            )

        scores = {name: 0 for name in professors_info}
        for i, ans in enumerate(answers):
            prof_name = questions[i]["options"][ans]
            scores[prof_name] += 1

        filtered_scores = {k: v for k, v in scores.items() if v > 0}
        max_val = max(filtered_scores.values()) if filtered_scores else 1
        names = list(filtered_scores.keys())
        values = list(filtered_scores.values())
        
        # 計算百分比
        total = sum(values)
        percents = [(val / total) * 100 for val in values]

        # 🎨 色彩配置 (最高分純黑，其餘深淺灰)
        base_grays = ['#bbbbbb', '#999999', '#777777', '#aaaaaa', '#888888']
        colors = []
        gray_idx = 0
        for val in values:
            if val == max_val:
                colors.append('#000000')
            else:
                colors.append(base_grays[gray_idx % len(base_grays)])
                gray_idx += 1

        # =========================================================
        # 📊 1. 產生純淨圓餅圖 (完全不含任何標籤與文字，避免方塊)
        # =========================================================
        fig, ax = plt.subplots(figsize=(6, 6), facecolor='#ffffff')
        ax.set_facecolor('#ffffff')
        explode = [0.1 if val == max_val else 0 for val in values]
        
        ax.pie(
            values, explode=explode, colors=colors,
            startangle=140, wedgeprops={'edgecolor': 'white', 'linewidth': 3}
        )
        
        # =========================================================
        # 📝 2. 生成標題 HTML
        # =========================================================
        title_html = "<h2 style='text-align: center; color: #000; font-weight: 900; font-size: 28px; margin-bottom: 20px; letter-spacing: 2px;'>📊 教授學術契合度分布</h2>"

        # =========================================================
        # 📝 3. 生成右側圖例 HTML (包含色塊、教授名字、百分比)
        # =========================================================
        legend_html = "<div style='display: flex; flex-direction: column; justify-content: center; gap: 15px; height: 100%; padding-left: 20px;'>"
        for name, pct, color, val in zip(names, percents, colors, values):
            is_top = " (TOP MATCH)" if val == max_val else ""
            font_weight = "900" if val == max_val else "bold"
            text_color = "#000" if val == max_val else "#555"
            
            legend_html += f"""
            <div style='display: flex; align-items: center; font-size: 18px; font-weight: {font_weight}; color: {text_color};'>
                <div style='width: 24px; height: 24px; background-color: {color}; border-radius: 6px; margin-right: 15px; border: 1px solid #ddd;'></div>
                <span>{name} - {pct:.1f}% <span style='font-size: 12px; color: #ff0055;'>{is_top}</span></span>
            </div>
            """
        legend_html += "</div>"

        # =========================================================
        # 📝 4. 生成推薦報告 HTML
        # =========================================================
        recommended_profs = [p for p, s in scores.items() if s == max_val]
        report_html = "<div style='margin-top: 40px;'><h2 style='text-align: center; color: #000; font-weight: 900; font-size: 28px; margin-bottom: 30px; letter-spacing: 2px;'>🎯 為您推薦的主力指導教授</h2>"

        for prof in recommended_profs:
            info = professors_info[prof]
            reqs = professors_reqs[prof]
            photo_url = professors_photos[prof]
            ndltd_url = f"https://www.google.com/search?q={urllib.parse.quote(f'site:ndltd.ncl.edu.tw \"{prof}\" 元智大學 工業工程與管理')}"

            report_html += f"""
            <div style='background: #fff; border: 3px solid #000; border-radius: 20px; padding: 35px; margin-bottom: 40px; box-shadow: 6px 6px 0px #000; position: relative; overflow: hidden;'>
                <div style='display: flex; flex-direction: column; align-items: center; margin-bottom: 30px; border-bottom: 2px solid #eaeaea; padding-bottom: 30px;'>
                    <div style='width: 140px; height: 140px; border-radius: 50%; border: 4px solid #000; box-shadow: 0 8px 20px rgba(0,0,0,0.15); overflow: hidden; margin-bottom: 20px;'><img src='{photo_url}' style='width: 100%; height: 100%; object-fit: cover;'></div>
                    <div style='text-align: center;'><h3 style='margin: 0 0 10px 0; color: #000; font-size: 34px; font-weight: 900; letter-spacing: 1px;'>{prof} <span style='font-size: 22px; color: #555;'>教授</span></h3><span style='font-weight: 900; color: #fff; font-size: 13px; background: #000; padding: 6px 16px; border-radius: 30px; letter-spacing: 2px;'>TOP MATCH</span></div>
                </div>
                <div style='margin-bottom: 25px;'>
                    <p style='color: #000; font-size: 17px; margin: 15px 0; line-height: 1.6;'><b style='background: #eee; padding: 6px 12px; border-radius: 8px; margin-right: 12px; display: inline-block;'>📖 研究領域</b> {info['field']}</p>
                    <p style='color: #000; font-size: 17px; margin: 15px 0; line-height: 1.6;'><b style='background: #eee; padding: 6px 12px; border-radius: 8px; margin-right: 12px; display: inline-block;'>💡 適合對象</b> {info['intro']}</p>
                </div>
                <div style='background: #fafafa; border-radius: 12px; padding: 20px; border: 2px dashed #bbb; margin-bottom: 30px;'>
                    <h4 style='color: #000; font-weight: 900; font-size: 16px; margin-top: 0; margin-bottom: 12px;'>⚠️ 先修課程與能力門檻評估</h4>
                    <p style='color: #222; font-size: 15px; margin: 10px 0; line-height: 1.6;'><b style='background: #000; color: #fff; padding: 4px 10px; border-radius: 6px; margin-right: 10px; font-size: 13px;'>建議先修</b> {reqs['course']}</p>
                    <p style='color: #222; font-size: 15px; margin: 10px 0; line-height: 1.6;'><b style='background: #000; color: #fff; padding: 4px 10px; border-radius: 6px; margin-right: 10px; font-size: 13px;'>核心能力</b> {reqs['skill']}</p>
                </div>
                <div style='background: #fcfcfc; border-radius: 15px; padding: 25px; border: 2px solid #eee; margin-bottom: 30px;'>
                    <h4 style='color: #000; font-weight: 900; font-size: 18px; margin-top: 0; margin-bottom: 20px; border-left: 6px solid #000; padding-left: 12px;'>📚 歷年指導論文庫 (精選)</h4>
                    <ul style='color: #444; padding-left: 25px; list-style-type: decimal; line-height: 1.9; font-size: 15px; font-weight: bold; margin: 0;'>
            """
            for paper in professors_papers[prof]: report_html += f"<li style='margin-bottom: 8px;'>{paper}</li>"
            report_html += f"</ul></div><div style='text-align: right; margin-top: 10px;'><a href='{ndltd_url}' target='_blank' style='display:inline-block; padding:14px 28px; background-color:#000; color:#fff; text-decoration:none; border-radius:50px; font-weight:900; font-size:15px; border:2px solid #000; box-shadow: 0 4px 10px rgba(0,0,0,0.15); transition: all 0.2s;' onmouseover=\"this.style.transform='translateY(-2px)';\" onmouseout=\"this.style.transform='translateY(0)';\">🔍 前往博碩士論文網搜尋此教授</a></div></div>"
        report_html += "</div>"
        
        plt.close(fig) # 釋放記憶體
        return (gr.update(visible=False, value=""), gr.update(visible=False), gr.update(visible=True), title_html, fig, legend_html, report_html)
    except Exception as e:
        error_msg = traceback.format_exc()
        crash_html = f"<div style='color: red; padding: 20px; border: 2px solid red; background: #ffe6e6;'><h3>後端發生異常錯誤</h3><pre>{error_msg}</pre></div>"
        return (
            gr.update(visible=True, value=crash_html), 
            gr.update(visible=True), gr.update(visible=False), 
            gr.update(value=""), gr.update(value=None), gr.update(value=""), gr.update(value="")
        )

# ==========================================
# 🎨 增強版 CSS：確保背景乾淨、圖表排版漂亮
# ==========================================
css = """
    body, html, main, .gradio-container, .contain, .wrap { background-color: #ffffff !important; }
    body.dark { background-color: #ffffff !important; }
    footer { display: none !important; }
    button[aria-label="Copy"], button[aria-label="Fullscreen"], .svelte-11ht8k, .action-buttons, .copy-button { display: none !important; }
    .gradio-html { border: none !important; box-shadow: none !important; background: transparent !important; }
    
    .form, .panel, .block, .svelte-112innx { background-color: transparent !important; border: none !important; box-shadow: none !important; }
    #main-layout { background-color: transparent !important; }

    .quiz-panel { background: #ffffff !important; border: 3px solid #000 !important; border-radius: 1.5rem !important; padding: 40px !important; box-shadow: 6px 6px 0px #000 !important; }
    .gradio-radio { background: transparent !important; border: none !important; box-shadow: none !important; margin-bottom: 30px !important; }
    .gradio-radio > span { font-size: 22px !important; font-weight: 900 !important; color: #000000 !important; margin-bottom: 15px !important; display: block !important; }
    .gradio-radio label { background-color: #fff !important; border: 2px solid #e0e0e0 !important; border-radius: 12px !important; padding: 12px 20px !important; cursor: pointer !important; transition: all 0.2s ease !important; }
    .gradio-radio label span { font-weight: bold !important; font-size: 15px !important; color: #555 !important; }
    .gradio-radio label:hover { border-color: #000 !important; transform: translateY(-2px); }
    .gradio-radio label:has(input:checked) { background-color: #000 !important; border-color: #000 !important; box-shadow: 3px 3px 0px #e0e0e0 !important; }
    .gradio-radio label:has(input:checked) span { color: #fff !important; }
    .tabs { border-bottom: 3px solid #000 !important; margin-bottom: 25px !important; }
    .tab-nav button { font-weight: 900 !important; font-size: 16px !important; color: #888 !important; border: none !important; padding: 15px 25px !important; background: transparent !important; }
    .tab-nav button.selected { color: #000 !important; border-bottom: 5px solid #000 !important; }
    .btn-submit { background: #000 !important; color: #fff !important; border-radius: 50px !important; font-weight: 900 !important; font-size: 20px !important; padding: 25px 0 !important; border: 2px solid #000 !important; margin-top: 30px !important; cursor: pointer !important; transition: all 0.3s ease !important;}
    .btn-submit:hover { background: #fff !important; color: #000 !important; box-shadow: 5px 5px 0px #000 !important; transform: translateY(-3px); }
"""

js_func = "function() { document.body.classList.remove('dark'); }"

print("⏳ [2/2] 正在建置使用者介面...")

with gr.Blocks(css=css, js=js_func, title="YuanZe IEM - Education") as app:
    gr.HTML("<div style='text-align: center; margin-top: 50px; margin-bottom: 40px;'><div style='text-transform: uppercase; font-size: 15px; color: #555; font-weight: 900; letter-spacing: 6px; margin-bottom: 12px;'>YuanZe IEM // Education Board</div><h1 style='font-size: 4.5rem; font-weight: 900; color: #000; margin: 0; letter-spacing: -2px;'>EDUCATION®</h1></div>")
    radio_inputs = []
    
    with gr.Row(elem_id="main-layout"):
        # 測驗區塊
        with gr.Column(elem_classes="quiz-panel", visible=True) as quiz_col:
            error_msg = gr.HTML(visible=False, elem_classes="gradio-html")
            gr.HTML("<h3 style='font-size: 26px; font-weight: 900; color: #000; margin-bottom: 10px; border-left: 6px solid #000; padding-left: 15px;'>📝 專題教授適性測驗</h3><p style='font-size: 16px; color: #555; font-weight: bold; margin-bottom: 30px; padding-left: 15px;'>請完成下方 10 題測驗，系統將自動為您生成推薦分析報表。</p>")
            with gr.Tabs():
                with gr.TabItem("探索 (Q1-Q3)"):
                    gr.HTML("<div style='height: 20px;'></div>")
                    for q in questions[0:3]: radio_inputs.append(gr.Radio(choices=list(q["options"].keys()), label=q["q"], elem_classes="gradio-radio"))
                with gr.TabItem("能力 (Q4-Q6)"):
                    gr.HTML("<div style='height: 20px;'></div>")
                    for q in questions[3:6]: radio_inputs.append(gr.Radio(choices=list(q["options"].keys()), label=q["q"], elem_classes="gradio-radio"))
                with gr.TabItem("職涯 (Q7-Q10)"):
                    gr.HTML("<div style='height: 20px;'></div>")
                    for q in questions[6:10]: radio_inputs.append(gr.Radio(choices=list(q["options"].keys()), label=q["q"], elem_classes="gradio-radio"))
            submit_btn = gr.Button("🚀 提交並生成專屬推薦報表", elem_classes="btn-submit")

        # 結果區塊
        with gr.Column(visible=False, elem_classes="quiz-panel") as result_col:
            # 1. HTML 標題
            chart_title = gr.HTML(elem_classes="gradio-html")
            
            # 2. 將圓餅圖與 HTML 圖例並排顯示
            with gr.Row():
                with gr.Column(scale=1):
                    plot_output = gr.Plot(show_label=False)
                with gr.Column(scale=1):
                    legend_output = gr.HTML(elem_classes="gradio-html")
            
            # 3. 推薦教授詳細資料
            html_output = gr.HTML(elem_classes="gradio-html")
            reset_btn = gr.Button("🔄 重新進行測驗", elem_classes="btn-submit")

    # 綁定按鈕事件 (注意 outputs 對應數量的修改)
    submit_btn.click(
        fn=analyze_results, 
        inputs=radio_inputs, 
        outputs=[error_msg, quiz_col, result_col, chart_title, plot_output, legend_output, html_output]
    )
    
    reset_btn.click(
        fn=lambda: (
            gr.update(visible=False, value=""), 
            gr.update(visible=True), gr.update(visible=False), 
            gr.update(value=""), gr.update(value=None), gr.update(value=""), gr.update(value="")
        ), 
        inputs=None, 
        outputs=[error_msg, quiz_col, result_col, chart_title, plot_output, legend_output, html_output]
    )

print("✅ 啟動專屬網頁伺服器...")

port = int(os.environ.get("PORT", 7860))
app.launch(server_name="0.0.0.0", server_port=port)
