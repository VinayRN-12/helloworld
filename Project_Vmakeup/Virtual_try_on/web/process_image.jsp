
<%@page import="Logic.info"%>

<%@page import="java.io.FileReader"%>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.io.IOException"%>
<%@page import="Logic.copy"%>
<%@page import="java.io.FileWriter"%>
<%@page import="java.io.FileOutputStream"%>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.io.File"%>
<%@page import="java.io.BufferedOutputStream"%>
<%@page import="java.util.Enumeration"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@page import="java.io.BufferedInputStream"%>

<%
    
try{
    
            
            
            String dirName=info.path;
            String paramname="";
            try
                {
		
                        String abPath="",sPath="",pptpath="";
                        BufferedInputStream  bis = null; 
                        BufferedOutputStream bos = null;
			MultipartRequest multi = new MultipartRequest(request, dirName,	10 * 1024 * 1024); 
                        Enumeration params = multi.getParameterNames();
			while (params.hasMoreElements()) 
			{
				paramname = (String) params.nextElement();
                                
                               
                        }
                        Enumeration files = multi.getFileNames();	
                        while (files.hasMoreElements()) 
                        {
                            paramname = (String) files.nextElement();
                            if(paramname.equals("d1"))
                            {
                                paramname = null;
                            }
                            if(paramname != null && paramname.equals("file"))
                            {
                               
                               pptpath = multi.getFilesystemName(paramname);
                               String fPath = dirName+pptpath;
                               session.setAttribute("fname", pptpath);
                               System.out.println("file>>>>>"+fPath);
                                 if(!fPath.contains("null"))  
                                 {
                                    File file = new File(fPath);
                                    FileInputStream fsR = new FileInputStream(file);
                                    byte[] b3=new byte[fsR.available()];
                                    
                                    
                                    String newPath=info.path+"input.png";
                                    FileOutputStream fout=new FileOutputStream(newPath);
                                    int j=0;
                                       while((j=fsR.read())!=-1)
                                       {

                                       fout.write((byte)j);

                                       }
                                       fsR.close();
                                       fout.close();
                                 }
                              }
                        }
                        
                        
                }catch(Exception e)
                {
                e.printStackTrace();
                }
            
            File fs=new File(info.path+"input.png");
            File fd=new File(info.py_path+"input.png");
            
            copy.copyFileUsingStream(fs,fd);
            
            
            Thread.sleep(1000);
            System.out.println("Process image");
String blue=session.getAttribute("blue").toString();
System.out.println("blue="+blue);
String green=session.getAttribute("green").toString();
System.out.println("green="+green);
String red=session.getAttribute("red").toString();
System.out.println("red="+red);
String product_category=session.getAttribute("product_category").toString();
System.out.println("product_category="+product_category);    
            File fnew0=new File(info.py_path+"color.txt");
                    FileWriter fw_new0=new FileWriter(fnew0);
                    fw_new0.write(blue+"#"+green+"#"+red);
                    fw_new0.close(); 
                    File fnew1=new File(info.py_path+"task.txt");
                    FileWriter fw_new1=new FileWriter(fnew1);
                    fw_new1.write(product_category);
                    fw_new1.close(); 
                     try {
                    Thread.sleep(5000);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
//                response.setContentType("text/plain");
//                response.getWriter().write("done");  

RequestDispatcher rd=null;
rd=request.getRequestDispatcher("result.jsp");
rd.forward(request, response);
            
        }catch(Exception e)
        {
        e.printStackTrace();
        }
   








%>