/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import Logic.copy;
import Logic.info;
import static Logic.info.path;
import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

@WebServlet("/ImageServlet")
public class ImageServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Get image data from request parameter
        String imageData = request.getParameter("image"); 
        System.out.println("imageData "+imageData);
        // Decode Base64 image data
        byte[] decodedImage = java.util.Base64.getDecoder().decode(imageData.split(",")[1]);
        System.out.println(".."+decodedImage.toString());
        // Save image to server
        FileOutputStream fos = new FileOutputStream(path+"input.png");
        fos.write(decodedImage);
        fos.close();

        // Respond to client
       
        
        File fs=new File(path+"input.png");
                        File fd=new File(info.py_path+"input.png");
                        
                        
                        copy.copyFileUsingStream(fs,fd);
                        HttpSession session=request.getSession();
            System.out.println("Process image");
String blue=session.getAttribute("blue").toString();
System.out.println("blue="+blue);
String green=session.getAttribute("green").toString();
System.out.println("green="+green);
String red=session.getAttribute("red").toString();
System.out.println("red="+red);
String product_category=session.getAttribute("product_category").toString();
System.out.println("product_category="+product_category);         
        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            Logger.getLogger(ImageServlet.class.getName()).log(Level.SEVERE, null, ex);
        }
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
                response.setContentType("text/plain");
                response.getWriter().write("done");   
//                RequestDispatcher rd=request.getRequestDispatcher("result.jsp");
//                rd.forward(request, response);
                     
    }
}
