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
    public partial class Form2 : Form
    {
        EventHandler<EventArgs> handler;
        List<Product> products = new List<Product>();
        bool added = false;
        public Form2()
        {
            InitializeComponent();
            handler = new EventHandler<EventArgs>(productsListbx_DoubleClick);
        }

        public DialogResult ShowDialog(List<Product> _products, EventHandler<EventArgs> _handler)
        {
            products = _products;
            if (!added)
            {
                productsListbx.Items.AddRange(products.ToArray());
                added = true;
            }

            handler = _handler;
            return ShowDialog();
        }

        private void productsListbx_DoubleClick(object sender, EventArgs e)
        {
            Product product = productsListbx.SelectedItem as Product;
            handler.Invoke(product, e);
            this.Close();
        }
    }
}
