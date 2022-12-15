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

namespace FlowDocuments
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            //Заголовок
            Run run1 = new Run("Сало для українців");
            Paragraph paragraph1 = new Paragraph(new Bold(run1));
            paragraph1.FontSize = 30;


            Paragraph paragraph2 = new Paragraph();
            //картинка
            Image img = new Image();
            BitmapImage bimg = new BitmapImage();
            bimg.BeginInit();
            bimg.UriSource = new Uri("..\\..\\Salo.jpg", UriKind.Relative);
            bimg.EndInit();
            img.Source = bimg;
            BlockUIContainer block = new BlockUIContainer(img);
            Figure fig = new Figure(block);
            fig.Width = new FigureLength(200);
            fig.HorizontalAnchor = FigureHorizontalAnchor.ContentRight;

            //текст
            Run run2 = new Run();
            run2.Text = "В українській культурі сало набуло дещо культового значення. " +
            "Як національна страва, воно стоїть поряд з такими безсумнівними візитними картками української кухні як борщ, вареники, голубці, галушки. " +
            "Сало є унікальною стравою у тому сенсі, що більшість народів вживає смалець, а українці їдять його великими і малими шматками, " +
            "часто з хлібом, часником та солоними овочами. Українське сало і любов українців до нього є предметом великої кількості жартів та фольклорних історій. ";
            paragraph2.Inlines.Add(fig);
            paragraph2.Inlines.Add(run2);

            Run run3 = new Run();
            run3.Text = "Сало здавна користувалося в нашому народі особливою популярністю. Йому віддавали перевагу, навіть не підозрюючи, що воно містить багато корисних речовин, " +
            "таких необхідних для людського організму. І, насамперед, — арахідонову кислоту, яка належить до ненасичених жирів і бере участь в " +
            "утворенні багатьох гормонів, а, отже, в холестериновому обміні.";
            Paragraph paragraph3 = new Paragraph(run3);

            //ссылки
            Run run4 = new Run("Матеріал взято з ");
            Hyperlink hp = new Hyperlink(new Run("http://uk.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BB%D0%BE"));
            hp.NavigateUri = new Uri("http://uk.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BB%D0%BE");
            Paragraph paragraph4 = new Paragraph();
            paragraph4.Inlines.Add(run4);
            paragraph4.Inlines.Add(hp);

            FlowDocument doc = new FlowDocument();
            doc.Blocks.Add(paragraph1);
            doc.Blocks.Add(paragraph2);
            doc.Blocks.Add(paragraph3);
            doc.Blocks.Add(paragraph4);

            DocReader.Document = doc;

        }
    }
}
