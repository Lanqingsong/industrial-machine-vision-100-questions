# 工业与机器视觉 100 问｜Q1–Q100

本仓库收录《工业与机器视觉100问》第三版 Q1–Q100 的 Markdown 正文、配图和站点配置。

这本书面向想学习工业视觉、准备相关面试，或需要参与视觉项目的读者，内容从相机、镜头、光源等硬件选型讲起，延伸到算法、PLC 通信和系统集成。每个问题都配有示意图、公式或代码，方便把单个器件和参数放回完整的视觉系统中理解，也方便按问题查找和复习。全书按统一目录、图片路径和站点结构组织。

## 阅读入口

- [关于这本书与全书结构](docs/preface.md)

当前发布内容按以下章节文件阅读；完整的 Q1–Q100 结构见[扉页说明](docs/preface.md)。

按章节阅读：

1. [第一章：相机、镜头与成像硬件选型（Q1–Q30）](docs/chapters/chapter-01-q01-q30.md)
2. [第二章：算法基础与系统验收（Q31–Q40）](docs/chapters/chapter-02-q31-q40.md)
3. [第三章：PLC、通信与运动控制（Q41–Q55）](docs/chapters/chapter-03-q41-q55.md)
4. [第四章：PLC 通信、实时控制与系统集成（Q56–Q60）](docs/chapters/chapter-04-q56-q60.md)
5. [第五章：PLC 通信、实时控制与系统集成（Q61–Q70）](docs/chapters/chapter-05-q61-q70.md)
6. [第六章：算法工程、软件架构与项目交付（Q71–Q80）](docs/chapters/chapter-06-q71-q80.md)
7. [第七章：软件架构、权限与项目成本（Q81–Q90）](docs/chapters/chapter-07-q81-q90.md)
8. [第八章：开发库、部署与运行维护（Q91–Q100）](docs/chapters/chapter-08-q91-q100.md)

## PDF 阅读版

- [下载《工业与机器视觉100问》Q51–Q100 第三版 PDF](output/pdf/工业与机器视觉100问_Q51-Q100_第三版.pdf)

本目录的 PDF 为 Q51–Q100 正式分册，采用 A4 页面、正式封面、分册说明页、题号书签、图片水印、页脚页码和统一元数据。

仓库内 Q1–Q100 图片已统一加入浅色版权标识：右上角为“LanQS｜工业与机器视觉100问”，右下角为“B站搜索：飒飒青屿”。

## 相关视频

- [在哔哩哔哩搜索“飒飒青屿”](https://search.bilibili.com/all?keyword=%E9%A3%92%E9%A3%92%E9%9D%92%E5%B1%BF)

## 逐题索引

README 下方列出 Q1–Q100 全部问题，可直接跳转到对应章节。

- [Q1：工业相机选型的三个最核心参数是什么？它们的计算公式或选择逻辑是怎样的？](docs/chapters/chapter-01-q01-q30.md#q01)
- [Q2：如何根据最小检测缺陷尺寸和视野范围，计算所需相机的最低分辨率？](docs/chapters/chapter-01-q01-q30.md#q02)
- [Q3：全局快门与卷帘快门的根本区别是什么？为什么动态工业检测通常优先选择全局快门？卷帘快门在什么情况下可以使用？](docs/chapters/chapter-01-q01-q30.md#q03)
- [Q4：相机的信噪比（SNR）是什么？它如何影响弱光成像？](docs/chapters/chapter-01-q01-q30.md#q04)
- [Q5：什么是相机的动态范围？在什么场景下需要高动态范围（HDR）相机？](docs/chapters/chapter-01-q01-q30.md#q05)
- [Q6：GigE Vision、USB3 Vision、Camera Link 和 CoaXPress 各有什么优缺点？如何按距离、带宽和成本选型？](docs/chapters/chapter-01-q01-q30.md#q06)
- [Q7：镜头的焦距、光圈（F值）、工作距离、视野之间有什么关系？如何根据工作距离和视野计算所需焦距？](docs/chapters/chapter-01-q01-q30.md#q07)
- [Q8：什么是镜头的景深？哪些因素影响景深？在检测厚度不一致的物体时，如何保证成像清晰？](docs/chapters/chapter-01-q01-q30.md#q08)
- [Q9：什么是远心镜头？它和普通镜头相比有什么优势？在什么场景下必须使用？](docs/chapters/chapter-01-q01-q30.md#q09)
- [Q10：C接口和CS接口镜头的区别是什么？接错了会怎样？](docs/chapters/chapter-01-q01-q30.md#q10)
- [Q11：什么是镜头畸变？它对测量精度有什么影响？如何校正？](docs/chapters/chapter-01-q01-q30.md#q11)
- [Q12：什么是像素当量（或像元精度）？如何计算？](docs/chapters/chapter-01-q01-q30.md#q12)
- [Q13：线阵相机和面阵相机分别适用于什么场景？为什么纺织品检测常用线阵相机？](docs/chapters/chapter-01-q01-q30.md#q13)
- [Q14：线阵相机的"行频"是什么？如何根据产线速度和检测精度计算所需的最小行频？](docs/chapters/chapter-01-q01-q30.md#q14)
- [Q15：什么是频闪光源？为什么要用它？它和连续光源在控制上有什么区别？](docs/chapters/chapter-01-q01-q30.md#q15)
- [Q16：请说出至少五种常见的光源类型（如环形光、同轴光、背光、条形光、穹顶光）及其最适用的检测场景。](docs/chapters/chapter-01-q01-q30.md#q16)
- [Q17：什么是明场照明和暗场照明？为什么暗场更适合检测透明物体表面的划痕？](docs/chapters/chapter-01-q01-q30.md#q17)
- [Q18：在检测高反光金属表面时，通常采用什么照明方式来消除反光？](docs/chapters/chapter-01-q01-q30.md#q18)
- [Q19：偏振片在视觉系统中的作用是什么？如何使用？](docs/chapters/chapter-01-q01-q30.md#q19)
- [Q20：如何为视觉系统选择合适的光源颜色（如红、蓝、绿、白、红外）？蓝色光源为什么常用于检测金属表面？](docs/chapters/chapter-01-q01-q30.md#q20)
- [Q21：光源的亮度不稳定会对算法产生什么影响？如何避免？](docs/chapters/chapter-01-q01-q30.md#q21)
- [Q22：如何评价一个照明方案的好坏？现场调试照明时，主要调整哪些参数？](docs/chapters/chapter-01-q01-q30.md#q22)
- [Q23：3D视觉常用哪些技术方案？（如双目立体视觉、结构光、激光三角测量、TOF）](docs/chapters/chapter-01-q01-q30.md#q23)
- [Q24：结构光 3D 相机的工作原理是什么？适用于检测物体的哪些特性？](docs/chapters/chapter-01-q01-q30.md#q24)
- [Q25：红外相机和紫外相机分别用于检测什么类型的缺陷？](docs/chapters/chapter-01-q01-q30.md#q25)
- [Q26：什么是智能相机？它与相机+工控机方案相比，优劣势是什么？](docs/chapters/chapter-01-q01-q30.md#q26)
- [Q27：如何阅读一份相机或镜头的官方数据手册？你会最关注哪些参数？](docs/chapters/chapter-01-q01-q30.md#q27)
- [Q28：相机需要散热吗？在高温车间如何保证相机稳定运行？](docs/chapters/chapter-01-q01-q30.md#q28)
- [Q29：振动环境对相机安装有什么要求？](docs/chapters/chapter-01-q01-q30.md#q29)
- [Q30：什么是光学防抖？工业相机需要这个功能吗？](docs/chapters/chapter-01-q01-q30.md#q30)
- [Q31：拿到一个新的检测项目，你的硬件选型（相机、镜头、光源）的具体步骤是什么？](docs/chapters/chapter-02-q31-q40.md#q31)
- [Q32：什么是手眼标定（Hand-Eye Calibration）？Eye-In-Hand 和 Eye-To-Hand 的区别是什么？](docs/chapters/chapter-02-q31-q40.md#q32)
- [Q33：什么是模板匹配？NCC、SAD、形状匹配的原理和适用场景有何不同？](docs/chapters/chapter-02-q31-q40.md#q33)
- [Q34：什么是 Blob 分析？如何用它完成连通域计算、面积筛选和工业缺陷定位？](docs/chapters/chapter-02-q31-q40.md#q34)
- [Q35：图像预处理的标准工具链是什么？滤波、形态学操作各解决什么问题？](docs/chapters/chapter-02-q31-q40.md#q35)
- [Q36：什么是 OCR 和 OCV？如何检测字符、条码、二维码的可读性和正确性？](docs/chapters/chapter-02-q31-q40.md#q36)
- [Q37：什么是 MTF（调制传递函数）？如何用它评价镜头和相机系统的真实解像力？](docs/chapters/chapter-02-q31-q40.md#q37)
- [Q38：什么是无监督异常检测（Anomaly Detection）？在没有缺陷样本的情况下如何训练工业检测模型？](docs/chapters/chapter-02-q31-q40.md#q38)
- [Q39：什么是双目立体视觉的视差（Disparity）？如何从视差图计算深度？误差来源有哪些？](docs/chapters/chapter-02-q31-q40.md#q39)
- [Q40：视觉系统项目验收时，客户通常提出哪些标准？如何设计完整的量产前验收测试方案？](docs/chapters/chapter-02-q31-q40.md#q40)
- [Q41：PLC 在机器视觉系统中最核心的作用是什么？请说明“触发—采集—处理—输出”的完整协同流程。](docs/chapters/chapter-03-q41-q55.md#q41)
- [Q42：什么是硬触发？什么是软触发？为什么工业现场主要使用硬触发？](docs/chapters/chapter-03-q41-q55.md#q42)
- [Q43：硬触发通常使用什么电平信号？NPN/PNP 和 24 V 应如何理解？](docs/chapters/chapter-03-q41-q55.md#q43)
- [Q44：PLC、光电传感器、视觉系统和剔除机构之间如何接线并协同控制？](docs/chapters/chapter-03-q41-q55.md#q44)
- [Q45：光电传感器、接近开关和光纤传感器的触发特性有什么区别？](docs/chapters/chapter-03-q41-q55.md#q45)
- [Q46：视觉系统通过什么方式将检测结果（OK/NG）告诉PLC？通常使用什么类型的输出模块？](docs/chapters/chapter-03-q41-q55.md#q46)
- [Q47：什么是光耦隔离？I/O模块为什么需要它？](docs/chapters/chapter-03-q41-q55.md#q47)
- [Q48：除了简单的I/O信号，视觉系统与PLC还有哪些通信方式？（如RS232/485、以太网TCP/IP、Modbus TCP/RTU、PROFINET）](docs/chapters/chapter-03-q41-q55.md#q48)
- [Q49：什么是Modbus通信中的寄存器、线圈、保持寄存器和输入寄存器？视觉系统如何映射检测结果？](docs/chapters/chapter-03-q41-q55.md#q49)
- [Q50：在什么情况下会选择通过工业以太网而不是简单I/O与PLC交互？](docs/chapters/chapter-03-q41-q55.md#q50)
- [Q51：什么是PROFINET或EtherCAT？视觉系统能接入这种总线吗？](docs/chapters/chapter-03-q41-q55.md#q51)
- [Q52：产线的运动控制（如伺服电机）是由PLC做还是由视觉系统做？视觉引导定位（如机器人抓取）时，数据流是怎样的？](docs/chapters/chapter-03-q41-q55.md#q52)
- [Q53：如何处理因传输延迟或处理时间导致的“定位偏差”？什么是“飞拍”或“跟踪触发”？](docs/chapters/chapter-03-q41-q55.md#q53)
- [Q54：什么是编码器？如何利用编码器信号实现更精准的触发或图像拼接？](docs/chapters/chapter-03-q41-q55.md#q54)
- [Q55：当产线速度变化时，如何保证视觉系统的触发频率同步变化？](docs/chapters/chapter-03-q41-q55.md#q55)
- [Q56：在多工位视觉检测系统中，如何协调多台相机与 PLC 的触发时序？](docs/chapters/chapter-04-q56-q60.md#q56)
- [Q57：视觉系统判断 NG 后，剔除装置（如气缸、推杆、摆臂）的动作通常由谁控制？延迟如何计算？](docs/chapters/chapter-04-q56-q60.md#q57)
- [Q58：什么是 HMI？视觉系统需要与 HMI 交互哪些信息？](docs/chapters/chapter-04-q56-q60.md#q58)
- [Q59：如何在 HMI 上设计便于操作工使用的视觉参数调整界面？（如 ROI 框、阈值滑块）](docs/chapters/chapter-04-q56-q60.md#q59)
- [Q60：生产换型时，视觉系统如何快速切换程序和参数？PLC 如何配合？](docs/chapters/chapter-04-q56-q60.md#q60)

### Q61–Q70
- [Q61：视觉系统发生故障（如相机断开）时，如何通知 PLC 使产线安全停机？](docs/chapters/chapter-05-q61-q70.md#q61)
- [Q62：如何为视觉系统设计心跳信号，以监控其在线状态？](docs/chapters/chapter-05-q61-q70.md#q62)
- [Q63：什么是 MES？视觉系统应该向 MES 上传哪些数据？](docs/chapters/chapter-05-q61-q70.md#q63)
- [Q64：如何让视觉系统的时钟与工厂网络时钟保持同步？](docs/chapters/chapter-05-q61-q70.md#q64)
- [Q65：为什么信号线和电源线要分开敷设？如果无法避免交叉，应怎样处理？](docs/chapters/chapter-05-q61-q70.md#q65)
- [Q66：车间环境光变化（早晚阳光、附近设备闪光）会怎样影响视觉系统？有哪些缓解策略？](docs/chapters/chapter-05-q61-q70.md#q66)
- [Q67：普通生产中的颜色、纹理和位置出现小幅正常波动时，视觉系统应该怎样处理？](docs/chapters/chapter-05-q61-q70.md#q67)
- [Q68：产品表面的油污和水渍应该怎样处理？算法能做什么，硬件能预防什么？](docs/chapters/chapter-05-q61-q70.md#q68)
- [Q69：振动会使图像模糊，除了延长曝光和全局快门，还有哪些措施有效？](docs/chapters/chapter-05-q61-q70.md#q69)
- [Q70：什么是“黄金样本”？它在调试和维护中起什么作用？](docs/chapters/chapter-05-q61-q70.md#q70)

### Q71–Q80
- [Q71：如何设计训练集采集流程，覆盖正常变化和缺陷条件？](docs/chapters/chapter-06-q71-q80.md#q71)
- [Q72：现场调试发现特定角度或光照下的误检，却无法稳定复现，应该怎么办？](docs/chapters/chapter-06-q71-q80.md#q72)
- [Q73：如何评价视觉系统的稳定性？除准确率外，还应监控哪些指标？](docs/chapters/chapter-06-q71-q80.md#q73)
- [Q74：工业检测中漏检和误检哪个更严重？算法如何平衡两者？](docs/chapters/chapter-06-q71-q80.md#q74)
- [Q75：什么是算法鲁棒性？如何提高检测算法的鲁棒性？](docs/chapters/chapter-06-q71-q80.md#q75)
- [Q76：深度学习模型部署到工业计算机后达不到节拍要求，应该从哪些方面优化？](docs/chapters/chapter-06-q71-q80.md#q76)
- [Q77：什么是模型量化、剪枝和知识蒸馏？它们分别解决什么问题？](docs/chapters/chapter-06-q71-q80.md#q77)
- [Q78：工业 PC 与普通 PC 有什么区别？为什么工厂更常选 IPC？](docs/chapters/chapter-06-q71-q80.md#q78)
- [Q79：工业 PC 上运行哪些操作系统？为什么许多工业软件仍然运行在 Windows 上？](docs/chapters/chapter-06-q71-q80.md#q79)
- [Q80：视觉系统必须 7×24 运行，如何设计自动启动和看门狗机制？](docs/chapters/chapter-06-q71-q80.md#q80)

### Q81–Q90
- [Q81：工业视觉系统如何管理软件版本和参数配置文件？](docs/chapters/chapter-07-q81-q90.md#q81)
- [Q82：现场人员可能误操作，工业视觉系统应该如何设计权限？](docs/chapters/chapter-07-q81-q90.md#q82)
- [Q83：客户要求增加一种缺陷检测，软件架构如何支持快速扩展？](docs/chapters/chapter-07-q81-q90.md#q83)
- [Q84：工业视觉项目交付时应该准备哪些文档？](docs/chapters/chapter-07-q81-q90.md#q84)
- [Q85：如何估算工业视觉项目的总体成本？（硬件、软件、开发与维护）](docs/chapters/chapter-07-q81-q90.md#q85)
- [Q86：算法处理一帧需要 100 ms，但产线要求每 80 ms 得到一个结果，怎么办？](docs/chapters/chapter-07-q81-q90.md#q86)
- [Q87：相机或镜头的性能会随时间退化，系统怎样检测并提前预警？](docs/chapters/chapter-07-q81-q90.md#q87)
- [Q88：什么是数据增强？除普通旋转和缩放外，工业视觉还有哪些针对性方法？](docs/chapters/chapter-07-q81-q90.md#q88)
- [Q89：缺陷样本极少、类别严重不平衡时，如何进行分类？](docs/chapters/chapter-07-q81-q90.md#q89)
- [Q90：传统算法和深度学习都能解决问题时，如何选择技术路线？](docs/chapters/chapter-07-q81-q90.md#q90)

### Q91–Q100
- [Q91：除了 OpenCV，还应该了解哪些商业或开源视觉开发库（例如 HALCON、VisionPro、MIL 和 AForge.NET）？](docs/chapters/chapter-08-q91-q100.md#q91)
- [Q92：HALCON 相比 OpenCV 有什么优势？许可证模式又该怎样理解？](docs/chapters/chapter-08-q91-q100.md#q92)
- [Q93：视觉开发应选 Python 还是 C++？两者在工业部署中的优缺点是什么？](docs/chapters/chapter-08-q91-q100.md#q93)
- [Q94：如何把 Python 训练的深度学习模型部署到 C++ 生产系统？](docs/chapters/chapter-08-q91-q100.md#q94)
- [Q95：TensorRT、OpenVINO 和 ONNX Runtime 分别是什么？在项目中各自扮演什么角色？](docs/chapters/chapter-08-q91-q100.md#q95)
- [Q96：在 Jetson、ARM 板卡等边缘设备上部署视觉算法，有哪些特殊考虑？](docs/chapters/chapter-08-q91-q100.md#q96)
- [Q97：如何设计多线程或多进程的视觉采集、处理程序？通常需要哪些线程（例如采集线程、处理线程、通信线程）？](docs/chapters/chapter-08-q91-q100.md#q97)
- [Q98：如果图像采集缓冲区大小设置不当，会出现哪些问题？](docs/chapters/chapter-08-q91-q100.md#q98)
- [Q99：如何实现生产者—消费者模式来处理图像队列？](docs/chapters/chapter-08-q91-q100.md#q99)
- [Q100：程序应该如何记录事件？工业现场实际需要哪些日志（错误、警告、逐帧结果、生产统计）？](docs/chapters/chapter-08-q91-q100.md#q100)

## 正文节选与配图

目录之后，放几段正文节选，方便读者先通过实际内容了解本书的写法和深度。

### 远心镜头：尺寸测量为什么关心几何稳定性？

远心镜头在工业视觉中受到重视，核心原因是普通镜头在尺寸测量和轮廓判定中会产生透视误差。当测量结果依赖边缘位置、放大倍率稳定性和遮挡关系时，远心镜头解决的是几何成像中的透视偏差，关注重点是尺寸和位置的精确性。

远心镜头通过特殊光学设计，使物方主光线在有效工作范围内近似平行于光轴。目标在小范围内前后移动时，图像中的尺寸变化远小于普通镜头，这对尺寸测量和轮廓提取尤为关键。相应的代价是前组镜片直径、成本和安装空间通常更高。

![普通镜头与远心镜头的成像几何对比](docs/chapters/images/q01-q30/Q9/fig9_01_telecentric_vs_normal_zh.png)

### 光源选择：先看目标特征，再决定灯的形式

环形光由环状分布的 LED 阵列构成，照明方向围绕镜头轴线对称展开，适合在较短工作距离内提供均匀、稳定、阴影较轻的正向照明。对于电子元件外观、标签字符、平面印刷、孔位定位和小型塑料件装配检查，环形光通常是上手较快、调试成本较低的方案。

同轴光通过分光镜把光沿镜头光轴方向投向工件，适合平整、高反射、局部细节依赖反射方向差异来区分的表面。背光主要服务于轮廓、孔径和外形尺寸，条形光适合方向性划痕和纹理，穹顶光则更适合复杂高反射曲面。

![五类常见工业视觉光源及其典型场景](docs/chapters/images/q01-q30/Q16/part3_16_01_lighting_types_compare.png)

### 明场与暗场：差别来自反射光是否进入镜头

明场照明的本质，是让来自平整背景的主要反射光进入镜头。平整区域因此较亮，目标与背景之间的差异主要来自反射率、吸收率或颜色差异。暗场照明让光线以较低角度入射，使平整表面的镜面反射避开镜头接收范围；划痕、毛刺、边缘、颗粒和其他几何突变产生的散射光进入镜头后，特征反而会变亮。

明场和暗场描述的是照明与成像的几何关系，环形光、同轴光、条形光和穹顶光描述的是具体硬件形式。同一类灯具在不同角度、工作距离和镜头数值孔径下，可能形成不同的成像效果。

![明场照明与暗场照明的反射几何对比](docs/chapters/images/q01-q30/Q17/part3_17_01_brightfield_darkfield.png)

### 高反光金属：先控制反射路径，再处理眩光

高反光金属表面的棘手之处在于镜面反射会把无关光强烈送入镜头。局部过曝会遮盖划痕、压痕、蚀刻、打码和污渍信息，工件姿态的轻微变化也可能造成灰度大幅波动，进而影响阈值和边缘提取的重复性。

同轴光可以把平整区域的反射变成较稳定的背景信号，让刻蚀、凹坑、划痕和局部倾斜面表现为暗特征；交叉偏振则可压低部分镜面眩光。两者都需要根据材料表面、入射角、缺陷方向和相机动态范围进行验证，单纯增加光强往往会放大高光问题。

![交叉偏振抑制高反光表面眩光的计算示例](docs/chapters/images/q01-q30/Q18/fig18_02_cross_polarization_worked_example_zh.png)

## 作者与开源协议

**作者：** 兰青松（网络署名：LanQS）  
**联系邮箱：** [874953727@qq.com](mailto:874953727@qq.com)

本仓库的出版正文与配图采用 [知识共享署名—非商业性使用—禁止演绎 4.0 国际许可协议（CC BY-NC-ND 4.0）](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)。在遵守协议并保留作者署名、作品名称和发布地址的前提下，允许个人阅读、学习和非商业分享；商业出版、付费培训、实质性改编和大规模再发布须事先取得作者书面许可。

引用建议：兰青松，《工业与机器视觉100问》第三版，引用具体章节或问题时请附本仓库地址。
