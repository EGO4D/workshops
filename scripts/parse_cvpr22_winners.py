import pyperclip


raw = """
Challenge: Ego4D Audio-Visual Diarization Challenge

1st Place: Intel Labs 
Team: 
Kyle Min, Intel Labs
Validation Report: https://arxiv.org/abs/2210.07764
Code: https://github.com/SRA2/SPELL

Challenge: Audio-Only Diarization Challenge

1st Place: pyannote
Team: 
Hervé Bredin, IRIT, Université de Toulouse, CNRS
Validation report: https://huggingface.co/pyannote/speaker-diarization
Code: https://huggingface.co/pyannote/speaker-diarization

2nd Place: diart
Team: 
Juan M. Coria, Universite Paris-Saclay CNRS, LISN
Sahar Ghannay, Universite Paris-Saclay CNRS, LISN
Validation report: https://github.com/juanmc2005/StreamingSpeakerDiarization/blob/ego4d/ego4d.pdf
Code: https://github.com/juanmc2005/StreamingSpeakerDiarization/tree/ego4d

3rd Place: Red Panda@IMAGINE
Team: 
Yin-Dong Zheng, Nanjing University
Guo Chen, Nanjing University, Shanghai AI Laboratory
Jiahao Wang, Nanjing University
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.08708
Code: https://github.com/Echo0125/Ego4d_Audio-only_Diarization_2022_3rd_Place_Solution
 

Challenge: AV Transcription Challenge

1st Place:  AVATAR-Google
Team: 
Paul Hongsuck Seo, Google Research
Arsha Nagrani, Google Research
Cordelia Schmid, Google Research
Validation report: https://arxiv.org/pdf/2211.09966.pdf

Challenge: Visual Queries 2D Localization

1st Place: Thereisnospoon
Team: 
Mengmeng Xu, KAUST
Juan-Manuel Perez-Rua, Facebook
Cheng-Yang Fu, Facebook
Yanghao Li, Facebook
 Bernard Ghanem, KAUST
Tao Xiang, Facebook
Validation report: https://arxiv.org/abs/2211.10528 
Code: https://github.com/facebookresearch/vq2d_cvpr


Challenge: Visual Queries 3D Localization

1st Place: IVUL
Team: 
Jinjie Mai, KAUST
Chen Zhao, KAUST
Abdullah Hamdi, KAUST
Silvio Giancola, KAUST
Bernard Ghanem, KAUST 
Validation report: https://arxiv.org/pdf/2211.10284.pdf
Code: https://github.com/Wayne-Mai/VQ3D_ECCVW2022

2nd Place: Thereisnospoon
Team: 
Mengmeng Xu, KAUST
Juan-Manuel Perez-Rua, Facebook
Cheng-Yang Fu, Facebook
Yanghao Li, Facebook
 Bernard Ghanem, KAUST
Tao Xiang, Facebook
Validation report: https://arxiv.org/abs/2211.10528
Code: https://github.com/facebookresearch/vq2d_cvpr

Challenge: Natural Language Queries

1st Place: VideoIntern
Team: 
Guo Chen, Shanghai AI Laboratory, Nanjing University
Jiahao Wang, Nanjing University
Yi Liu, SIAT, Shanghai AI Laboratory
Yifei Huang, University of Tokyo
Jiashuo Yu, Shanghai AI Laboratory
Yi Wang, Shanghai AI Laboratory
Yali Wang, SIAT, Shanghai AI Laboratory
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Yu Qiao, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.09529
Code: https://github.com/OpenGVLab/ego4d-eccv2022-solutions

2nd Place: University of Wisconsin-Madison
Team: 
Sicheng Mo, University of Wisconsin-Madison
Fangzhou Mu, University of Wisconsin-Madison
Yin Li, University of Wisconsin-Madison
Validation report: https://arxiv.org/pdf/2211.08704.pdf


3rd Place: COarse-to-fiNE alignment framework (CONE)
Team: 
Zhijian Hou, City University of Hong Kong
Wanjun Zhong, Sun Yat-sen University
Lei Ji, Microsoft Research Asia
Difei Gao, National University of Singapore
Kun Yan, Beihang University
Wing-Kwong Chan, City University of Hong Kong
Chong-Wah Ngo, Singapore Management University
Zheng Shou, National University of Singapore
Nan Duan,  Microsoft Research Asia
Validation report: https://arxiv.org/pdf/2211.08776.pdf
Code: https://github.com/houzhijian/CONE.

Challenge: Moments Queries

1st Place: VideoIntern
Team: 
Guo Chen, Shanghai AI Laboratory, Nanjing University
Jiahao Wang, Nanjing University
Yi Liu, SIAT, Shanghai AI Laboratory
Yifei Huang, University of Tokyo
Jiashuo Yu, Shanghai AI Laboratory
Yi Wang, Shanghai AI Laboratory
Yali Wang, SIAT, Shanghai AI Laboratory
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Yu Qiao, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.09529
Code: https://github.com/OpenGVLab/ego4d-eccv2022-solutions
2nd Place: University of Wisconsin-Madison
Team: 
Fangzhou Mu, University of Wisconsin-Madison
 Sicheng Mo, University of Wisconsin-Madison
Gillian Wang, University of Wisconsin-Madison
Yin Li, University of Wisconsin-Madison
Validation report: https://arxiv.org/pdf/2211.09074.pdf
Code: https://github.com/happyharrycn/actionformer_release

3rd Place: ReLER@ZJU
Team: 
Jiayi Shao, ReLER Lab, CCAI, Zhejiang University
Xiaohan Wang, ReLER Lab, CCAI, Zhejiang University
Yi Yang, ReLER Lab, CCAI, Zhejiang University
Validation report: https://arxiv.org/abs/2211.09558
Code: https://github.com/JonnyS1226/Ego4d_mq_3rd_solution

Challenge: Looking at Me 

1st Place: PKU-WICT-MIPL
Team: 
Xiyu Wei, Wangxuan Institute of Computer Technology, Peking University
Dejie Yang, Wangxuan Institute of Computer Technology, Peking University
Minghang Zheng, Wangxuan Institute of Computer Technology, Peking University
Qingchao Chen, National Institute of Health Data Science, Peking University
Yuxin Peng, Wangxuan Institute of Computer Technology, Peking University 
Yang Liu, Wangxuan Institute of Computer Technology, Peking University; Beijing Institute for General Artificial Intelligence
Code: https://github.com/lemon-prog123/Ego4D-ECCV-LAM

2nd Place: KeioEgo
Team: 
Haowen Hu, Graduate School of Science and Technology, Keio University
Ryo Hachiuma, Graduate School of Science and Technology, Keio University 
Hideo Saito, Graduate School of Science and Technology, Keio University
Validation report: https://drive.google.com/file/d/1N8OsZ77gUTcGJ1s8TEjKk8T_o54Fifv5/view?usp=sharing
Research code: https://github.com/Huhaowen0130/EgoFlow

3rd Place: NPT
Team: 
Yinan He, Beijing University of Posts and Telecommunications
Guo Chen, State Key Lab for Novel Software Technology, Nanjing University
Validation report: https://github.com/yinanhe/ego4d-look-at-me/blob/master/NPT_LAM.pdf
Research code: https://github.com/yinanhe/ego4d-look-at-me

Challenge: Talking to Me 

1st Place: University of Texas at Austin & Meta AI 
Team: 
Zihui Xue, The University of Texas at Austin and Meta AI 
Yale Song, Meta AI 
Kristen Grauman, The University of Texas at Austin and Meta AI 
Validation report: Forthcoming 


Challenge: Long Term Action Anticipation

1st Place: Autonomous Systems 
Team: 
Esteve Valls Mascaro, Autonomous Systems, Technische Universitat Wien (TU Wien)
Hyemin Ahn, Ulsan National Institute of Science and Technology (UNIST)
Dongheui Lee, Autonomous Systems, Technische Universitat Wien (TU Wien) & Institute of Robotics and Mechatronics, German Aerospace Center (DLR)
Validation report: https://arxiv.org/abs/2207.12080

Challenge: Future Hand Prediction

1st Place: VideoIntern 
Team: 
Guo Chen, Shanghai AI Laboratory, Nanjing University
Yizhuo Li, The University of Hong Kong, Shanghai AI Laboratory
Kunchang Li, SIAT, Shanghai AI Laboratory
Yinan He, Shanghai AI Laboratory
Bingkun Huang, Nanjing University, Shanghai AI Laboratory
Yifei Huang, University of Tokyo
Yi Wang, Shanghai AI Laboratory
Yali Wang, SIAT, Shanghai AI Laboratory
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Yu Qiao, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.09529
Code: https://github.com/OpenGVLab/ego4d-eccv2022-solutions

2nd Place: KeioEgo
Team: 
Haowen Hu, Graduate School of Science and Technology, Keio University
Ryo Hachiuma, Graduate School of Science and Technology, Keio University 
Hideo Saito, Graduate School of Science and Technology, Keio University
Code: https://github.com/masashi-hatano/ego4d-fhp-challenge-2022

Challenge:  Short Term Object Interaction Anticipation 

1st Place: Video Intern 
Team: 
Sen Xing, Shanghai AI Laboratory, Tsinghua University
Guo Chen, Nanjing University, Shanghai AI Laboratory
Zhe Chen, Nanjing University, Shanghai AI Laboratory
Junting Pan, Chinese University of Hong Kong, Shanghai AI Laboratory
Yifei Huang, University of Tokyo
Yi Wang, Shanghai AI Laboratory
Yali Wang, SIAT, Shanghai AI Laboratory
Limin Wang, Nanjing University, Shanghai AI Laboratory
Yu Qiao, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.09529
Code: https://github.com/OpenGVLab/ego4d-eccv2022-solutions

Challenge: State Change Object Detection

1st Place: VideoIntern
Team: 
Guo Chen, Shanghai AI Laboratory, Nanjing University
Zhe Chen, Nanjing University, Shanghai AI Laboratory
Yi Wang, Shanghai AI Laboratory
Wenhai Wang, Shanghai AI Laboratory
Yali Wang, SIAT, Shanghai AI Laboratory
Limin Wang, Nanjing University, Shanghai AI Laboratory
Yu Qiao, Shanghai AI Laboratory
Validation report: https://arxiv.org/abs/2211.09529
Code: https://github.com/OpenGVLab/ego4d-eccv2022-solutions

Challenge: Object State Change Classification

1st Place: Red Panda@IMAGINE 
Team: 
Yin-Dong Zheng, Nanjing University
Guo Chen, Nanjing University, Shanghai AI Laboratory
Jiahao Wang, Nanjing University
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Validation report: https://arxiv.org/pdf/2211.08728.pdf

2nd Place: EgoMotion-COMPASS 
Team: 
Jianchen Lei, Zhejiang University 
Shuang Ma, Microsoft
Zhongjie Ba, Zhejiang University 
Kui Ren, Zhejiang University
Validation report: https://arxiv.org/abs/2211.15286
Code: https://github.com/jasonrayshd/egomotion


3rd Place: Pear Republic 
Team: 
Shijie Wang, Brown University  
Validation report: https://drive.google.com/file/d/1L8mEDXlStom-APCEkwfrNM0Vd5aGIGUp/view?usp=sharing


Challenge: PNR Temporal Localization

1st Place: Red Panda@IMAGINE 
Team: 
Yin-Dong Zheng, Nanjing University
Guo Chen, Nanjing University, Shanghai AI Laboratory
Jiahao Wang, Nanjing University
Tong Lu, Nanjing University
Limin Wang, Nanjing University, Shanghai AI Laboratory
Validation report: https://arxiv.org/pdf/2211.08728.pdf

2nd Place: EgoMotion-COMPASS
Team: 
Jianchen Lei, Zhejiang University 
Shuang Ma, Microsoft
Zhongjie Ba, Zhejiang University 
Kui Ren, Zhejiang University 
Valdition report: https://github.com/jasonrayshd/egomotion 

3rd Place: University of Texas at Austin & Meta AI 
Team: 
Zihui Xue, The University of Texas at Austin and Meta AI 
Yale Song, Meta AI 
Kristen Grauman, The University of Texas at Austin and Meta AI 
Validation report: Forthcoming 
"""

output_html = ""

evalai_links = {
    "Ego4D Audio-Visual Diarization Challenge": "https://eval.ai/web/challenges/challenge-page/1640/overview",
    "Audio-Only Diarization Challenge": "https://eval.ai/web/challenges/challenge-page/1641/overview",
    "AV Transcription Challenge": "https://eval.ai/web/challenges/challenge-page/1637/overview",
    "Visual Queries 2D Localization": "https://eval.ai/web/challenges/challenge-page/1843/overview",
    "Visual Queries 3D Localization": "https://eval.ai/web/challenges/challenge-page/1646/overview",
    "Moments Queries": "https://eval.ai/web/challenges/challenge-page/1626/overview",
    "Looking at Me": "https://eval.ai/web/challenges/challenge-page/1624/overview",
    "Talking to Me": "https://eval.ai/web/challenges/challenge-page/1625/overview",
    "Long Term Action Anticipation": "https://eval.ai/web/challenges/challenge-page/1598/overview",
    "Future Hand Prediction": "https://eval.ai/web/challenges/challenge-page/1630/overview",
    "Short Term Object Interaction Anticipation": "https://eval.ai/web/challenges/challenge-page/1623/overview",
    "State Change Object Detection": "https://eval.ai/web/challenges/challenge-page/1632/overview",
    "Natural Language Queries": "https://eval.ai/web/challenges/challenge-page/1629/overview",
    "Object State Change Classification": "https://eval.ai/web/challenges/challenge-page/1627/overview",
    "PNR Temporal Localization": "https://eval.ai/web/challenges/challenge-page/1622/overview",
}

newline = "\n"


def gen_html(context):
    x = f"""<tr>
        <td>{context['position']}</td>
        <td>
            <span class="winners-team-name">{context['team_name']}</span>
        <ul>
            {
                newline.join([
                    f'<li>{member}</li>' for member in context['team_members']
                ])
            }
        </ul>
        </td>
        <td>
        {
            f"<a href={context['validation_report']}>Validation Report</a>" if "Forthcoming" not in context['validation_report'] else "Forthcoming"
        }
        </td>
        <td>
        {
            f"<a href={context['code']}>Code</a>" if "Forthcoming" not in context['code'] else "Forthcoming"
        }
        </td>
    </tr>
    """

    return x


context = {}
last_context = ""

for line in raw.split("\n"):
    if line.startswith("Challenge"):
        if context.get("challenge") is not None:
            output_html += gen_html(context)
            output_html += "</table>"
        context["challenge"] = line.split(":")[1].strip()
        output_html += f"""
<a href={evalai_links[context['challenge']]}><h4 class="small-title align-center">{context['challenge']} <i class="fas fa-link"></i></h4></a>
<table class="winners-table">
    <tr>
        <th>Place</th>
        <th>Team</th>
        <th>Validation Report</th>
        <th>Code</th>
    </tr>"""
        last_context = "challenge"

    elif line.lower().startswith("team"):
        context["team_members"] = []
        last_context = "team_members"

    elif line.lower().startswith("validation report"):
        context["validation_report"] = line[line.index(":") + 1 :]
        last_context = "validation_report"

    elif line.lower().startswith("code"):
        context["code"] = line[line.index(":") + 1 :]
        last_context = "code"

    elif line.lower().startswith("1st place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "1st Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif line.lower().startswith("2nd place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "2nd Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif line.lower().startswith("3rd place"):
        if last_context != "challenge":
            output_html += gen_html(context)
        context["position"] = "3rd Place"
        context["team_name"] = line.split(":")[1].strip()
        last_context = "position"

    elif len(line) > 1:
        context["team_members"].append(line.strip())

output_html += gen_html(context)
output_html += "</table>"

print(output_html)
pyperclip.copy(output_html)
