import torch
import torch.nn.functional as F

def get_noise_schedule(T, beta_start=1e-4, beta_end=0.02):
    """
    Linear schedule of betas from beta_start to beta_end over T steps.
    """
    return torch.linspace(beta_start, beta_end, T)

def q_sample(x_start, t, noise, alphas_cumprod):
    """
    Sample from q(x_t | x_0), i.e., add noise to the input image x_start at timestep t.
    """
    sqrt_alphas_cumprod = torch.sqrt(alphas_cumprod[t])[:, None, None, None]
    sqrt_one_minus_alphas_cumprod = torch.sqrt(1 - alphas_cumprod[t])[:, None, None, None]
    return sqrt_alphas_cumprod * x_start + sqrt_one_minus_alphas_cumprod * noise

def add_noise(x_start, T, device="cpu"):
    """
    Returns a list of images from 0 to T steps of added noise
    """
    betas = get_noise_schedule(T).to(device)
    alphas = 1.0 - betas
    alphas_cumprod = torch.cumprod(alphas, dim=0)

    noisy_images = []
    for t in range(T):
        noise = torch.randn_like(x_start)
        t_tensor = torch.tensor([t], device=device)
        noisy_img = q_sample(x_start, t_tensor, noise, alphas_cumprod)
        noisy_images.append(noisy_img)
    return noisy_images