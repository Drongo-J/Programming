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

namespace Grid_sample
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        public Window1()
        {
            InitializeComponent();
            this.Title = "Grid Sample";

            //Grid определяет гибкую область сетки, состоящую из столбцов и строк.
            Grid myGrid = new Grid();
            myGrid.Width = 500;
            myGrid.Height = 500;
            myGrid.HorizontalAlignment = HorizontalAlignment.Center;
            myGrid.VerticalAlignment = VerticalAlignment.Center;
            myGrid.ShowGridLines = true;

            // Создаем столбцы
            // ColumnDefinition определяет свойства столбца, которые применяются к элементам Grid.
            ColumnDefinition colDef1 = new ColumnDefinition();
            ColumnDefinition colDef2 = new ColumnDefinition();
            ColumnDefinition colDef3 = new ColumnDefinition();
            myGrid.ColumnDefinitions.Add(colDef1);
            myGrid.ColumnDefinitions.Add(colDef2);
            myGrid.ColumnDefinitions.Add(colDef3);

            // Создаем строки
            // RowDefinition определяет свойства конкретной строки, которые применяются к элементам Grid
            RowDefinition rowDef1 = new RowDefinition();
            RowDefinition rowDef2 = new RowDefinition();
            RowDefinition rowDef3 = new RowDefinition();
            RowDefinition rowDef4 = new RowDefinition();
            myGrid.RowDefinitions.Add(rowDef1);
            myGrid.RowDefinitions.Add(rowDef2);
            myGrid.RowDefinitions.Add(rowDef3);
            myGrid.RowDefinitions.Add(rowDef4);

            // TextBlock обеспечивает упрощенное управление отображением небольшого количества потока содержимого
            // Добавляем текстовый блок в нулевую ячейку нулевой строки
            TextBlock txt1 = new TextBlock();
            txt1.Text = "2013 Products Shipped";
            txt1.FontSize = 20;
            txt1.FontWeight = FontWeights.Bold;
            Grid.SetColumnSpan(txt1, 3);// объединяются три соседние ячейки
            Grid.SetRow(txt1, 0); 

            // Добавляем текстовый блок в нулевую ячейку первой строки
            TextBlock txt2 = new TextBlock();
            txt2.Text = "Quarter 1";
            txt2.FontSize = 12;
            txt2.FontWeight = FontWeights.Bold;
            Grid.SetRow(txt2, 1);
            Grid.SetColumn(txt2, 0);

            // Добавляем текстовый блок в первую ячейку первой строки
            TextBlock txt3 = new TextBlock();
            txt3.Text = "Quarter 2";
            txt3.FontSize = 12;
            txt3.FontWeight = FontWeights.Bold;
            Grid.SetRow(txt3, 1);
            Grid.SetColumn(txt3, 1);

            // Добавляем текстовый блок во вторую ячейку первой строки
            TextBlock txt4 = new TextBlock();
            txt4.Text = "Quarter 3";
            txt4.FontSize = 12;
            txt4.FontWeight = FontWeights.Bold;
            Grid.SetRow(txt4, 1);
            Grid.SetColumn(txt4, 2);

            // Добавляем текстовый блок в нулевую ячейку второй строки
            TextBlock txt5 = new TextBlock();
            double db1 = 50000;
            txt5.Text = db1.ToString();
            Grid.SetRow(txt5, 2);
            Grid.SetColumn(txt5, 0);

            // Добавляем текстовый блок в первую ячейку второй строки
            TextBlock txt6 = new TextBlock();
            double db2 = 100000;
            txt6.Text = db2.ToString();
            Grid.SetRow(txt6, 2);
            Grid.SetColumn(txt6, 1);

            // Добавляем текстовый блок во вторую ячейку второй строки
            TextBlock txt7 = new TextBlock();
            double db3 = 150000;
            txt7.Text = db3.ToString();
            Grid.SetRow(txt7, 2);
            Grid.SetColumn(txt7, 2);

            // Добавляем текстовый блок в нулевую ячейку третьей строки
            TextBlock txt8 = new TextBlock();
            txt8.FontSize = 16;
            txt8.FontWeight = FontWeights.Bold;
            txt8.Text = "Total Units: " + (db1 + db2 + db3).ToString();
            Grid.SetRow(txt8, 3);
            Grid.SetColumnSpan(txt8, 3);// объединяются три соседние ячейки

            myGrid.Children.Add(txt1);
            myGrid.Children.Add(txt2);
            myGrid.Children.Add(txt3);
            myGrid.Children.Add(txt4);
            myGrid.Children.Add(txt5);
            myGrid.Children.Add(txt6);
            myGrid.Children.Add(txt7);
            myGrid.Children.Add(txt8);

            // элемент Grid является содержимым главного окна
            this.Content = myGrid;
         

        }
    }
}
