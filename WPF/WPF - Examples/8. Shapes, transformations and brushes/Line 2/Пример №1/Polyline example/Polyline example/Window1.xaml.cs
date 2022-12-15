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
        public Window1()
        {
            InitializeComponent();
            // Add the Polyline Element
            Polyline myPolyline = new Polyline();
            myPolyline.Stroke = Brushes.SlateGray;
            myPolyline.StrokeThickness = 2;
            myPolyline.FillRule = FillRule.EvenOdd;
            Point Point1 = new Point(10, 150);
            Point Point2 = new Point(30, 140);
            Point Point3 = new Point(50, 160);
            Point Point4 = new Point(70, 130);
            Point Point5 = new Point(90, 170);
            Point Point6 = new Point(110, 120);
            Point Point7 = new Point(130, 180);
            Point Point8 = new Point(150, 110);
            Point Point9 = new Point(170, 190);
            Point Point10 = new Point(190, 100);
            Point Point11 = new Point(210, 240);
            PointCollection myPointCollection = new PointCollection();
            myPointCollection.Add(Point1);
            myPointCollection.Add(Point2);
            myPointCollection.Add(Point3);
            myPointCollection.Add(Point4);
            myPointCollection.Add(Point5);
            myPointCollection.Add(Point6);
            myPointCollection.Add(Point7);
            myPointCollection.Add(Point8);
            myPointCollection.Add(Point9);
            myPointCollection.Add(Point10);
            myPointCollection.Add(Point11);
            myPolyline.Points = myPointCollection;
            mygrid.Children.Add(myPolyline);



        }
    }
}
