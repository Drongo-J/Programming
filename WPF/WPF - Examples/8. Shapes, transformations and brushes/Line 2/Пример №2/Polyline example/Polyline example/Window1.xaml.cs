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
        const int revs = 20;
        const int numpts = 1000 * revs;
        Polyline poly;
        public Window1()
        {
            InitializeComponent();
            poly = new Polyline();
            poly.Stroke = SystemColors.WindowTextBrush;
            canv.Children.Add(poly);
            Point[] pts = new Point[numpts];
            for (int i = 0; i < numpts; i++)
            {
                double angle = i * 2 * Math.PI / (numpts / revs);
                double scale = 250 * (1 - (double)i / numpts);
                pts[i].X = scale * Math.Cos(angle);
                pts[i].Y = scale * Math.Sin(angle);
            }
            poly.Points = new PointCollection(pts);
        }

        private void canv_SizeChanged(object sender, SizeChangedEventArgs args)
        {
            Canvas.SetLeft(poly, args.NewSize.Width / 2);
            Canvas.SetTop(poly, args.NewSize.Height / 2);
        }
    }
}
   
