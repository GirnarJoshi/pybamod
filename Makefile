test:
	echo "Running tests in test_bamod.py"
	pytest test_bamod.py 

create_env:
	echo " ************************ "
	echo " Creating envornment "
	echo " ************************ "
	conda create -n bamod_env python=3.13 numpy pytest -y 
	echo " ************************ "
	echo " Environment Name [ bamo_env ] has been created "
	echo " ************************ "

env_activate:
	echo " ************************ "
	echo " Activating the Environment "
	echo " ************************ "
	conda activate bamod_env
	
	echo " ************************ "
	echo " ************************ "

env_deactivate: 
	conda deactivate
	echo " ************************ "
	echo " Environment has been Deactivated "
	echo " ************************ "
