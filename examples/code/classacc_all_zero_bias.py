from rlscore import core
from rlscore import reader
from rlscore import writer
from rlscore import measure

kwargs = {}
kwargs['train_labels'] = reader.read_dense('./examples/data/class_train.labels')
prediction_features = reader.read_sparse('./examples/data/class_test.features')
kwargs['train_features'] = reader.read_sparse('./examples/data/class_train.features')
test_labels = reader.read_dense('./examples/data/class_test.labels')
kwargs['reggrid'] = '-10_10'
kwargs['bias'] = '0'
kwargs['kernel'] = 'LinearKernel'
kwargs['learner'] = 'RLS'
measurefun = measure.accuracy
kwargs['measure'] = measurefun
kwargs['mselection'] = 'LOOSelection'
trainresults = core.trainModel(**kwargs)
model = trainresults['model']
print 'Making predictions on test data'
predicted_labels = model.predict(prediction_features)
performance = measurefun(test_labels, predicted_labels)
print 'Performance: %f %s' % (performance, measurefun.__name__)
writer.write_pickle('./examples/models/classacc.model', model)
writer.write_dense('./examples/predictions/classacc.predictions', predicted_labels)