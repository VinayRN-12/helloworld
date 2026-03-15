package admin;

import static Logic.ImageResizer.resizeImage;
import Logic.info;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;

import connection.DatabaseConnection;
import java.awt.Image;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

/**
 * Servlet implementation class AddProducts
 */
@WebServlet("/AddProducts")
public class AddProducts extends HttpServlet {
	private final String UPLOAD_DIRECTORY = info.path+"uploads/";
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
            try{
		HttpSession session = request.getSession();
                System.out.println("add product");
		//if (ServletFileUpload.isMultipartContent(request)) {
			try {
				List<FileItem> multiparts = new ServletFileUpload(new DiskFileItemFactory()).parseRequest(request);
				String imageName=null;
				String productName = null;
				String productQuantity = null;
				String productPrice =null;
				String descrip=null;
				String mrpPrice=null;
				String status=null;
				String category=null;
				String blue=null;
				String green=null;
				String red=null;
				String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		        StringBuilder salt = new StringBuilder();
		        Random rnd = new Random();
		        while (salt.length() < 3) { // length of the random string.
		            int index = (int) (rnd.nextFloat() * SALTCHARS.length());
		            salt.append(SALTCHARS.charAt(index));
		        }
		        String code = salt.toString();
				                        System.out.println("salt "+salt);
				for (FileItem item : multiparts) {
                                        if (!item.isFormField()) {
						imageName = new File(item.getName()).getName();
                                                System.out.println("imageName="+imageName);
                                                System.out.println(UPLOAD_DIRECTORY + File.separator + imageName);
						item.write(new File(UPLOAD_DIRECTORY + File.separator + imageName));
						FileItem pName = (FileItem) multiparts.get(0);
						productName = pName.getString();
						 System.out.println("productName "+productName);
						FileItem price = (FileItem) multiparts.get(1);
						productPrice = price.getString();	
					System.out.println("productPrice "+productPrice);
						
						FileItem description = (FileItem) multiparts.get(2);
						descrip = description.getString();
						  System.out.println("descrip "+descrip);
						
						FileItem mprice = (FileItem) multiparts.get(3);
						mrpPrice = mprice.getString();
						  System.out.println("mrpPrice "+mrpPrice);
						
						FileItem fstatus = (FileItem) multiparts.get(4);
						status = fstatus.getString();
						   System.out.println("status "+status);
						FileItem pcategory = (FileItem) multiparts.get(5);
						category = pcategory.getString();
                                                 System.out.println("category "+category);
                                                FileItem pblue = (FileItem) multiparts.get(6);
						blue = pblue.getString();
                                                System.out.println("blue "+blue);
                                                FileItem pgreen = (FileItem) multiparts.get(7);
						green = pgreen.getString();
                                                 System.out.println("green "+green);
                                                FileItem pred= (FileItem) multiparts.get(8);
						red = pred.getString();
							 System.out.println("red "+red);
					}
				}
                                
                              
                              
                             
                                
                                 
                                
                                
                                
                                
                                
				try {
					int id = 0;
					String imagePath = UPLOAD_DIRECTORY + imageName;
                                        String q="insert into tblproduct(id,active,code,description,image,image_name,name,price,mrp_price,product_category,blue,green,red) values('" + id+ "','" + status + "','"+code+"','" + descrip + "','" + imagePath + "','"+imageName+"','"+productName+"','"+productPrice+"','"+mrpPrice+"','"+category+"','"+blue+"','"+green+"','"+red+"')";
					System.out.println(q);
                                        int i = DatabaseConnection.insertUpdateFromSqlQuery(q);
					Image img = null;    
                                         BufferedImage tempPNG = null;
                                            BufferedImage tempJPG = null;
                                            File newFilePNG = null;
                                            File newFileJPG = null;
                                        img = ImageIO.read(new File(imagePath));
                tempPNG = resizeImage(img, 200, 200);
               // tempJPG = resizeImage(img, 200, 200);
                newFilePNG = new File(imagePath);
              
                ImageIO.write(tempPNG, "png", newFilePNG);
                                   
                                        if (i > 0) {
						String success = "Product added successfully.";
						session.setAttribute("message", success);
						response.sendRedirect("admin-add-product.jsp");
					}

				} catch (Exception e) {
					e.printStackTrace();
				}
			} catch (Exception ex) {
				request.setAttribute("message", "File Upload Failed due to " + ex);
			}

//		} else {
//			request.setAttribute("message", "Sorry this Servlet only handles file upload request");
//		}

        }catch(Exception e)
        {
        e.printStackTrace();
        }
	}
}
