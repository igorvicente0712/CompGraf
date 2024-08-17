import vtk

# Função para rotacionar o cubo ao redor de seu centro de massa
def rotate_around_center_of_mass(obj, event):
    key = obj.GetKeySym()
    step = 0.05
    if key == "4":
        transform_cube.Translate(step * -1, 0, 0)
    elif key == "6":
        transform_cube.Translate(step, 0, 0)
    elif key == "8":
        transform_cube.Translate(0, step, 0)
    elif key == "2":
        transform_cube.Translate(0, -step, 0)
    elif key == "5":
        transform_cube.Translate(0, 0, -step)
    elif key == "g":
        transform_cube.RotateZ(-5)
    elif key == "b":
        transform_cube.Scale(1.1,1.1,1.1)
    elif key == "n":
        transform_cube.Scale(0.9,0.9,0.9)
    elif key == "j":
        transform_cube.RotateZ(5) 
        renderWindow.Render()
    if key == "k":
        posn = actor_cube.GetPosition()    # aqui você captura a tecla que foi pressionada
    if key == "h":
        posn = actor_cube.GetPosition()                                              # captura a posição do cubo
        actor_cube.AddPosition(posn[0],posn[1],posn[2])               #trás de volta da origem (T)
        actor_cube.RotateZ(5)                                                                 # rotaciona no sentido anti-horário (R)
        actor_cube.AddPosition(-posn[0],-posn[1],-posn[2])             # leva para a origem (T’)
    renderWindow.Render()

# Definir o raio da esfera[]
sphere = vtk.vtkSphereSource()
sphere.SetRadius(0.2)
sphere.SetThetaResolution(32)
sphere.SetPhiResolution(32)
sphere.Update()

# Criar um cubo usando vtkCubeSource
cube = vtk.vtkCubeSource()
cube.SetXLength(1.0) # Largura do cubo no eixo X
cube.SetYLength(1.0) # Altura do cubo no eixo Y
cube.SetZLength(1.0) # Profundidade do cubo no eixo Z
cube.Update()

# Mapeador para o cubo
mapper_cube = vtk.vtkPolyDataMapper()
mapper_cube.SetInputConnection(cube.GetOutputPort())

mapper_sphere = vtk.vtkPolyDataMapper()
mapper_sphere.SetInputConnection(sphere.GetOutputPort())

# Ator para o cubo
actor_cube = vtk.vtkActor()
actor_cube.SetMapper(mapper_cube)
actor_cube.SetPosition(2, 2, 0) # Definir a posição inicial do cubo

actor_sphere = vtk.vtkActor()
actor_sphere.SetMapper(mapper_sphere)

# # Renderizador
renderer = vtk.vtkRenderer()
renderer.AddActor(actor_sphere)
renderer.AddActor(actor_cube)
renderer.SetBackground(0.0, 0.5, 0.0) # Cor de fundo

camera = renderer.GetActiveCamera()
camera.SetPosition(0, 0, 10)                     # Posição da câmera
camera.SetFocalPoint(0, 0, 0)                   # Ponto para onde a câmera está olhando
camera.SetViewUp(0, 1, 0)                        # Direção "para cima" da câmera

camera.SetViewAngle(60)                         # Campo de visão vertical (em graus)
camera.SetClippingRange(1.0, 20.0)        # Planos de clipping próximos e distantes

# Criar uma transformação para o ator
transform_cube = vtk.vtkTransform()

# Aplicar a transformação ao ator
actor_cube.SetUserTransform(transform_cube)

# Janela de renderização
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(800, 600)

# Interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

#CHAME A FUNÇÃO
# Associar a função de callback ao evento de tecla
renderWindowInteractor.AddObserver("KeyPressEvent", rotate_around_center_of_mass)

#START TODO O PROCESSO:
# Inicializar a visualização
renderWindow.Render()
renderWindowInteractor.Start()
