from app.services.roboflow_service import RoboflowService

def test_analyze_image(mocker):
    service = RoboflowService()
    mock_client = mocker.patch.object(service.client, 'infer')
    
    fake_bytes = b"test"
    service.analyze_image(fake_bytes)
    
    mock_client.assert_called_once()
    args, kwargs = mock_client.call_args
    assert isinstance(args[0], str)
    assert kwargs['model_id'] == "santabarbara/3"