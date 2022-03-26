using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;
using System.IO;
using System.Web;
using System.Net;


namespace AplikasiMonitoring
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string dataterima1, dataterima2, oksigen, ph1, suhu1, amonia1, ph2, suhu2, amonia2;
        string apiKey;
        double tagValue1, tagValue2, tagValue3, tagValue4, tagValue5, tagValue6, tagValue7;
        string server = "https://api.thingspeak.com/"; string webMethod; string uri;

        private void Form1_Load(object sender, EventArgs e)
        {
            foreach (String port in SerialPort.GetPortNames())
            {
                comboBox1.Items.Add(port);
               
            }
            foreach (String port in SerialPort.GetPortNames())
            {
                comboBox2.Items.Add(port);
            }
        }



        private void button1_Click(object sender, EventArgs e)
        {
            Port1.PortName = Convert.ToString(comboBox1.Text);
            Port1.Open();

            timer1.Start();


        }

        private void button2_Click(object sender, EventArgs e)
        {
            Port2.PortName = Convert.ToString(comboBox2.Text);
            Port2.Open();
            
        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            var webclient = new WebClient();
            apiKey = "SBK3Z2TZTYCHX0UP";

            string[] datapecah1;
            string[] datapecah2;
            dataterima1 = Port1.ReadLine();

            datapecah1 = dataterima1.Split(' ');
            
            oksigen = datapecah1[0];
            ph1 = datapecah1[1];
            suhu1 = datapecah1[2];
            amonia1 = datapecah1[3];

            textBox1.Text = oksigen + " mg/L ";
            textBox2.Text = ph1 + " ";
            textBox3.Text = suhu1 + " °C ";
            textBox4.Text = amonia1 + " g/L ";


            tagValue1 = Convert.ToDouble(oksigen);
            tagValue2 = Convert.ToDouble(ph1);
            tagValue3 = Convert.ToDouble(suhu1);
            tagValue4 = Convert.ToDouble(amonia1);            
            
            dataterima2 = Port2.ReadLine();

            datapecah2 = dataterima2.Split(' ');


            ph2 = datapecah2[0];
            suhu2 = datapecah2[1];
            amonia2 = datapecah2[2];

            textBox5.Text = ph2 + " ";
            textBox6.Text = suhu2 + " °C ";
            textBox7.Text = amonia2 + " g/L ";

            
            tagValue5 = Convert.ToDouble(ph2);
            tagValue6 = Convert.ToDouble(suhu2);
            tagValue7 = Convert.ToDouble(amonia2);            


            webMethod = "update?api_key=" + apiKey + "&field1=" + tagValue1 + "&field2=" + tagValue2 +
                       "&field3=" + tagValue3 + "&field4=" + tagValue4 + "&field5=" + tagValue5 + "&field6=" + tagValue6 + "&field7=" + tagValue7;
            uri = server + webMethod;
            webclient.UploadString(uri, "POST", ""); 
        }
                
    }
}
