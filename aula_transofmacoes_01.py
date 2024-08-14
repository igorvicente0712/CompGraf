import vtk

# função para transformações geométricas com o teclado
def meu_teclado (obj, event): # nome da função
    key = obj.GetKeySym() # aqui captura a tecla pressionada
    step = 0.05
    if key == "4":
        transform.Translate(step * -1, 0, 0)
    elif key == "6":
        transform.Translate(step, 0, 0)
    elif key == "8":
        transform.Translate(0, step, 0)
    elif key == "2":
        transform.Translate(0, -step, 0)
    elif key == "5":
        transform.Translate(0, 0, -step)
    elif key == "g":
        transform.RotateX(-10)
    elif key == "b":
        transform.Scale(1.1,1.1,1.1)
    elif key == "n":
        transform.Scale(0.9,0.9,0.9)
    renderWindow.Render() # Atualizar a renderização

# Leitura do arquivo OBJ
reader = vtk.vtkOBJReader()
reader.SetFileName(r"C:\Users\unieivicente\Downloads\Bambo_House.obj")
reader.Update()

# Mapeador
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

 # Ator
ator = vtk.vtkActor()
ator.SetMapper(mapper)

# Renderizador
renderer = vtk.vtkRenderer()
renderer.AddActor(ator)
renderer.SetBackground(0.1, 0.2, 0.3) # Cor de fundo

# Janela de renderização
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(800, 600)

transform = vtk.vtkTransform()
ator.SetUserTransform(transform)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#Associar a função de callback ao evento de tecla
renderWindowInteractor.AddObserver("KeyPressEvent", meu_teclado)

# Inicializar a visualização
renderWindow.Render()
renderWindowInteractor.Start()