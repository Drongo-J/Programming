using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Polyline_example
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
      
        Polyline poly;
        public Window1()
        {
            InitializeComponent();
            poly = new Polyline();
            poly.Stroke = SystemColors.WindowTextBrush;
            poly.VerticalAlignment = VerticalAlignment.Center;
            canv.Children.Add(poly);
            for (int i = 0; i < 2000; i++)
            {
                poly.Points.Add(new Point(i, 96 * (1 - Math.Sin(i * Math.PI / 192))));
            }
        }
    
    }
}
   
