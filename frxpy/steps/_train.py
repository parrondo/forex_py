# -*- coding: utf-8 -*-

import torch
import torch.optim

class Classifier(nn.Module):
    def __init__(self, model, criterion):
        super(Classifier, self).__init__()
        self.model = model
        self.criterion = criterion

    def __call__(self, x, t):
        out = self.model(x)
        loss = self.criterion(out, t)
        return loss
    

class MyTrainer(object):
    def __init__(self,
                 model,
                 classifier,
                 optimizer,
                 ngpu,
                 epochs,
    ):
        self.model = model
        self.classifier = classifier
        self.optimizer = optimizer
        self.model = Classifier(self.model, self.criterion)
        self.gpumode = False
        
        if npgu == 1:
            self.model.cuda()
            self.gpumode = True
        elif ngpu >= 2:
            gpus = [i for i in range(ngpu)]
            self.model = torch.nn.DataParallel(self.model, device_ids=gpus)
            self.model.cuda()
            self.gpumode = True            
        else:
            pass

    def set_optimizer(self,
                      optimizer: torch.optim = None,
                      **kwargs
    ):
        
        self.optimizer = optimizer(self.model.parameters(),
                                   **kwargs)
        
    def _train(self,
               mode,
               data_iter):
        assert mode.lower() in ['train', 'cv'], f'{mode} mode is not supported.'
        if mode.lower() == 'train':
            self.model.train()
        else:
            self.model.eval()

        for idx, idata in enumerate(data_iter):
            if self.gpumode:
                pass
        
    def train(self,
              train_iter: torch.utils.data.DataLoder,
              test_iter: torch.utils.data.DataLoder,
    ):
        for i in range(self.epochs):
            pass
    
