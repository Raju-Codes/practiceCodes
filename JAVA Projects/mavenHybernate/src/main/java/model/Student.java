package model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import javax.naming.Name;

@Entity
@Table(name = "Student")
public class Student {
    @Id
    @Column (name="Student ID")
    private Integer SId;

    @Column (name="Student Name")
    private String SName;

    @Column (name="Student City")
    private String SCity;

    @Column (name="Student Roll")
    private String Sroll;

    public Student() {
    }

    public Student(Integer SId, String SName, String SCity, String Sroll) {
        this.SId = SId;
        this.SName = SName;
        this.SCity = SCity;
        this.Sroll = Sroll;
    }

    public Integer getSId() {
        return SId;
    }

    public String getSName() {
        return SName;
    }

    public String getSCity() {
        return SCity;
    }

    public String getSroll() {
        return Sroll;
    }

    public void setSId(Integer SId) {
        this.SId = SId;
    }

    public void setSName(String SName) {
        this.SName = SName;
    }

    public void setSCity(String SCity) {
        this.SCity = SCity;
    }

    public void setSroll(String sroll) {
        Sroll = sroll;
    }

    @Override
    public String toString() {
        return "Student{" +
                "SId=" + SId +
                ", SName='" + SName + '\'' +
                ", SCity='" + SCity + '\'' +
                ", Sroll='" + Sroll + '\'' +
                '}';
    }
}


