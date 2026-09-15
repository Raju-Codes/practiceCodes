package App;

import model.Student;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class LaunchFirstApp {
    public static void main(String[] args){
        //Configuration object
        Configuration config = new Configuration();

        //configure hibernate.cf.xml file for configuration.
        config.configure();

        // Crate session factory
       SessionFactory sessionFactory = config.buildSessionFactory();

       //Get the object from the session Factory
        Session session = sessionFactory.openSession();

       Transaction transaction = session.beginTransaction();

        Student student = new Student();
        student.setSId(1);
        student.setSName("Raj");

        }
}
