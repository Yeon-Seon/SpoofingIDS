### ASD: ARP Spoofing Detector using OpenWrt
***
## Project Abstract
* ASD (ARP Spoofing Detector) can distinguish ARP spoofing attack attempts and network connections from a VM guest on a bridged network
* ASD was implemented on an OpenWrt-based AP and evaluated on its ability to handle ARP attacks without returning any false positive alarms
* ARP spoofing attack attempts can be monitored using a visualization tool provided in ASD.
    * Attack scenario for an ARP spoofing-based MITM attack
<img src="https://user-images.githubusercontent.com/48937186/156372876-73522be1-d297-4faf-bb17-5a6644fe6af4.PNG" width="700">   
    * System overview of ASD
<img src="https://user-images.githubusercontent.com/48937186/156372946-4fea3a60-4dbf-4b08-b2e8-40ee39bba738.PNG" width="700">   


## Experimental Setup

* Access Point: Xiaomi Mi Wi-Fi mini

<img src="https://img.danawa.com/prod_img/500000/928/180/img/3180928_1.jpg?shrink=500:500&_v=20150702112553" width="40%"></img>  

* OpenWrt Installation

```
https://m.blog.naver.com/PostView.nhn?blogId=love_tolty&logNo=221743172685&proxyReferer=https%3A%2F%2Fwww.google.com%2F
```

## ASD 
* Visualization tool of ASD
    * Normal Status
    ![image](https://user-images.githubusercontent.com/48937186/156372968-15449622-0772-4129-adb7-931a6016aa62.PNG)
    * VM Connection Status
    ![image](https://user-images.githubusercontent.com/48937186/156372971-4b81be90-13ab-40f5-ada3-490cabca645d.PNG)
    * ARP Spoofing Attack Status
    ![image](https://user-images.githubusercontent.com/48937186/156372974-6023be40-027f-40c8-a6d0-f1e64c377db3.PNG)


