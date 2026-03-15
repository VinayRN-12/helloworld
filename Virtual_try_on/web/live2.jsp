


<%@page import="Logic.info"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@ page import="connection.*"%>
<%@ page import="java.sql.*"%>
<!--
Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE html>
<html>

<!-- Mirrored from p.w3layouts.com/demos/apr-2016/05-04-2016/smart_shop/web/mens.html by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 23 Jul 2020 05:57:36 GMT -->
<!-- Added by HTTrack -->
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<!-- /Added by HTTrack -->
<head>
<title><%=info.name%></title>
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords"
	content="Smart Shop Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
<script type="application/x-javascript">
	
	
	
	
	
	
	 addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
		function hideURLbar(){ window.scrollTo(0,1); } 






</script>
<!-- //for-mobile-apps -->
<link href="css/bootstrap.css" rel="stylesheet" type="text/css"
	media="all" />
<link rel="stylesheet" type="text/css" href="css/jquery-ui.css">
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
<!-- js -->
<script type="text/javascript" src="js/jquery-2.1.4.min.js"></script>
<!-- //js -->
<!-- cart -->
<script src="js/simpleCart.min.js"></script>
<!-- cart -->
<!-- for bootstrap working -->
<script type="text/javascript" src="js/bootstrap-3.1.1.min.js"></script>
<!-- //for bootstrap working -->
<link href='http://fonts.googleapis.com/css?family=Montserrat:400,700'
	rel='stylesheet' type='text/css'>
<link
	href='http://fonts.googleapis.com/css?family=Lato:400,100,100italic,300,300italic,400italic,700,900,900italic,700italic'
	rel='stylesheet' type='text/css'>
<link rel="stylesheet"
	href="https://use.fontawesome.com/releases/v5.7.0/css/all.css"
	integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ"
	crossorigin="anonymous">
<script src="js/jquery.easing.min.js"></script>
</head>
<body>
	<script
		src='../../../../../../ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js'></script>
	<script
		src="../../../../../../m.servedby-buysellads.com/monetization.js"
		type="text/javascript"></script>
	<script>
		(function() {
			if (typeof _bsa !== 'undefined' && _bsa) {
				// format, zoneKey, segment:value, options
				_bsa.init('flexbar', 'CKYI627U', 'placement:w3layoutscom');
			}
		})();
	</script>
	<script>
		(function() {
			if (typeof _bsa !== 'undefined' && _bsa) {
				// format, zoneKey, segment:value, options
				_bsa.init('fancybar', 'CKYDL2JN', 'placement:demo');
			}
		})();
	</script>
	<script>
		(function() {
			if (typeof _bsa !== 'undefined' && _bsa) {
				// format, zoneKey, segment:value, options
				_bsa.init('stickybox', 'CKYI653J', 'placement:w3layoutscom');
			}
		})();
	</script>
	<!--<script>(function(v,d,o,ai){ai=d.createElement("script");ai.defer=true;ai.async=true;ai.src=v.location.protocol+o;d.head.appendChild(ai);})(window, document, "//a.vdo.ai/core/w3layouts_V2/vdo.ai.js?vdo=34");</script>-->
	<div id="codefund">
		<!-- fallback content -->
	</div>
	<script src="https://ethicalads.io/?ref=codefund" async="async"></script>

	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async
		src='https://www.googletagmanager.com/gtag/js?id=UA-149859901-1'></script>
<!--	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag() {
			dataLayer.push(arguments);
		}
		gtag('js', new Date());

		gtag('config', 'UA-149859901-1');
	</script>-->

<!--	<script>
		window.ga = window.ga || function() {
			(ga.q = ga.q || []).push(arguments)
		};
		ga.l = +new Date;
		ga('create', 'UA-149859901-1', 'demo.w3layouts.com');
		ga('require', 'eventTracker');
		ga('require', 'outboundLinkTracker');
		ga('require', 'urlChangeTracker');
		ga('send', 'pageview');
	</script>-->
	<script async src='../../../../../js/autotrack.js'></script>
    <% 
String projPath = request.getContextPath(); 
String productId=request.getParameter("productId").toString();
String productName=request.getParameter("productName").toString();
String image_name=request.getParameter("image_name").toString();
String price=request.getParameter("price").toString();
String mrp_price=request.getParameter("mrp_price").toString();
String blue=request.getParameter("blue").toString();
String green=request.getParameter("green").toString();
String red=request.getParameter("red").toString();
String product_category=request.getParameter("product_category").toString();
System.out.println("image_name>>>"+image_name);
session.setAttribute("product_category", product_category);
session.setAttribute("blue", blue);
session.setAttribute("green", green);
session.setAttribute("red", red);
%>
	<meta name="robots" content="noindex">
<body>
	<link rel="stylesheet"
		href="../../../../../images/demobar_w3_4thDec2019.css">
	<!-- Demo bar start -->
	<!-- header -->
	<!-- //header -->
	<!-- header-bot -->
	<div class="header-bot">
		<div class="container">
			<div class="col-md-3 header-left">
				<h1>
					<a href="index-2.html"><img src="images/logo3.jpg"></a>
				</h1>
			</div>
			<div class="col-md-6 header-middle">
				<form action="searchProduct.jsp" method="post">
					<div class="search">
						<input type="search"  name="search" placeholder="Search Product" style="width: 680px;">
					</div>
					<div class="sear-sub">
						<input type="submit" value=" ">
					</div>
					<div class="clearfix"></div>
				</form>
			</div>
			<div class="col-md-3 header-right footer-bottom">
				<ul>
					<li><a href="admin-login.jsp" style="width: 150px;"><i
							class="fas fa-user"></i>&nbsp;Admin Login</a></li>

				</ul>
			</div>
			<div class="clearfix"></div>
		</div>
	</div>
	<!-- //header-bot -->
	<!-- banner -->
	<div class="ban-top">
		<div class="container">
			<div class="top_nav_left">
				<nav class="navbar navbar-default">
					<div class="container-fluid">
						<!-- Brand and toggle get grouped for better mobile display -->
						<div class="navbar-header">
							<button type="button" class="navbar-toggle collapsed"
								data-toggle="collapse"
								data-target="#bs-example-navbar-collapse-1"
								aria-expanded="false">
								<span class="sr-only">Toggle navigation</span> <span
									class="icon-bar"></span> <span class="icon-bar"></span> <span
									class="icon-bar"></span>
							</button>
						</div>
						<!-- Collect the nav links, forms, and other content for toggling -->
						<jsp:include page="header.jsp"></jsp:include>
					</div>
				</nav>
			</div>
			<div class="top_nav_right">
				<div class="cart box_1">
 </div>
                        </div>
                </div>
        </div>
                                        <div style="display: flex; justify-content: center; align-items: center; height: 200px; ">
<!--                                        <div id="prod_image" >-->
                                             <image src="uploads/<%=image_name%>" width="200" height="200"></image>
                                        </div>
                                        <div style="display: flex; justify-content: center; align-items: center; height: 50px; ">
                                               <h1>Product Name <%=productName%></h1>
                                        </div>
                                        <div style="display: flex; justify-content: center; align-items: center; height: 50px; ">
                                               <h1>Price <%=price%></h1>
                                        </div>
                         
                            <div style="display: flex; justify-content: center; align-items: center; height: 50px; ">
                                             Capture Face Photo and AI will apply the product on your face   <%=productName%>
                                        </div>
                      
         <div style="display: flex; justify-content: center; align-items: center; height: 50px; ">
                                      
                                        </div>
                 
<div class="imageContainer"></div>
<!--        <div class="container" >   -->
          <div style="display: flex; justify-content: center; align-items: center; height: 500px; ">
            

                <form action="process_image.jsp" method="post" enctype="multipart/form-data" >
                <table>
                    
               <tr>
                   <td><label><h1>Upload Facial Image</h1></label></td>
                   <td><canvas id="canvas" width="640" height="480" style="display: none;"></canvas></td>
                  
                       
               </tr>
               <tr>
                   <td><input type="file"  name="file" id="file" /></td>
                   </tr>
                   <tr>
                       <td><input type="submit" name="submit" value="Proceed"/></td>
               </tr>
                <tr>
                    <td>
                         <video id="video" width="640" height="480" autoplay></video>
                    </td>
                  
                    <td>
                        <button id="captureButton">Capture and try</button>
                    </td>
               </tr>
        
                </table>   
            </form>       
                        
	
    
    
        
        </div>
        
        
        
        
        
                

          
	<script>
        // Get access to webcam
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                var video = document.getElementById('video');
                video.srcObject = stream;
            })
            .catch(function(err) {
                console.error('Error accessing webcam: ', err);
            });

        // Capture image from webcam
        document.getElementById('captureButton').addEventListener('click', function() {
            var video = document.getElementById('video');
            var canvas = document.getElementById('canvas');
            var context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            var imageData = canvas.toDataURL('image/jpeg');

            // Send captured image to servlet
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'ImageServlet', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log('Image sent successfully');
                    window.location.href = "result.jsp";
                }
            };
            xhr.send('image=' + encodeURIComponent(imageData));
        });
    </script>
</body>
</html>