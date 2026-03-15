
<%@page import="java.io.FileReader"%>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.io.FileWriter"%>
<%@page import="Logic.copy"%>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.io.OutputStream"%>
<%@page import="java.io.InputStream"%>
<%@page import="java.io.IOException"%>
<%@page import="Logic.info"%>
<%@page import="java.util.ArrayList"%>

<%@page import="java.awt.image.DataBufferByte"%>

<%@page import="java.awt.image.BufferedImage"%>
<%@page import="javax.imageio.ImageIO"%>
<%@page import="java.awt.Image"%>
<%@page import="java.util.Random"%>
<%@page import="java.io.FileOutputStream"%>
<%@page import="java.io.File"%>
<%@page import="java.util.Base64"%>
<%@page import="java.io.Reader"%>

<%
    System.out.println("Process image");
String blue=session.getAttribute("blue").toString();
System.out.println("blue="+blue);
String green=session.getAttribute("green").toString();
System.out.println("green="+green);
String red=session.getAttribute("red").toString();
System.out.println("red="+red);
String product_category=session.getAttribute("product_category").toString();
System.out.println("product_category="+product_category);
    String path=info.path;       


try
		{
			StringBuffer buffer = new StringBuffer();
			Reader reader = request.getReader();
			int current;

			while((current = reader.read()) >= 0)
			buffer.append((char) current);
			
			String data = new String(buffer);
			data = data.substring(data.indexOf(",") + 1);

			

			FileOutputStream output = new FileOutputStream(new File(path+"input.png"));

			output.write(Base64.getDecoder().decode(data));
			output.flush();
			output.close();
                        
                        File fs=new File(path+"input.png");
                        File fd=new File(info.py_path+"input.png");
                        
                        
                        copy.copyFileUsingStream(fs,fd);
                    
                        Thread.sleep(1000);
                    File fnew0=new File(info.py_path+"color.txt");
                    FileWriter fw_new0=new FileWriter(fnew0);
                    fw_new0.write(blue+"#"+green+"#"+red);
                    fw_new0.close(); 
                    File fnew1=new File(info.py_path+"task.txt");
                    FileWriter fw_new1=new FileWriter(fnew1);
                    fw_new1.write(product_category);
                    fw_new1.close(); 
                     try {
                    Thread.sleep(10000);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
                  
                RequestDispatcher rd=request.getRequestDispatcher("result.jsp");
                rd.forward(request, response);
                     
                     
                     
		}
		catch (Exception e)
		{
			e.printStackTrace();
                          System.out.println("error b");
		}

%>
<%
     

%>
