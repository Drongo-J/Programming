using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp6._1
{
    public partial class Form1 : Form
    {
        EventHandler<EventArgs> handler;
        public Form1()
        {
            InitializeComponent();
            Product product1 = new Product("Iphone", "Very Good", 2000);
            Product product2 = new Product("Samsung", "Good", 1000);
            Product product3 = new Product("Huawei", "Normal", 800);
            Product product4 = new Product("Xiamoi", "Bad", 500);
            products.Add(product1);
            products.Add(product2);
            products.Add(product3);
            products.Add(product4);
            handler = new EventHandler<EventArgs>(FillTextBoxes);

        }

        Form2 form2 = new Form2();
        List<Product> products = new List<Product>();
        private void button2_Click(object sender, EventArgs e)
        {
            if (productNameTxtb.Text != String.Empty && productDescriptionTxtb.Text != String.Empty && productPriceMtxtb.Text != String.Empty)
            {
                Product product = new Product(productNameTxtb.Text, productDescriptionTxtb.Text, double.Parse(productPriceMtxtb.Text));
                products.Add(product);
                this.Hide();

                if (form2.ShowDialog(products, handler) == DialogResult.Cancel)
                {
                    this.Show();
                }
            }
        }

        Product global_product;
        private void FillTextBoxes(object sender, EventArgs e)
        {
            var product = sender as Product;
            global_product = product;
            productNameTxtb.Text = product.Name;
            productDescriptionTxtb.Text = product.Description;
            productPriceMtxtb.Text = product.Price.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (global_product != null)
            {
                double.Parse(productPriceMtxtb.Text);
                global_product.Name = productNameTxtb.Text;
                global_product.Description = productDescriptionTxtb.Text;
                global_product.Price = double.Parse(productPriceMtxtb.Text); ;

                this.Hide();

                if (form2.ShowDialog(products, handler) == DialogResult.Cancel)
                {
                    this.Show();
                }
            }
        }
    }
}
