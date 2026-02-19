using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace BackendAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MarketController : ControllerBase
    {
        private readonly HttpClient _httpClient;

        public MarketController(IHttpClientFactory httpClientFactory)
        {
            _httpClient = httpClientFactory.CreateClient();
        }

        [HttpGet("{category}")]
        public async Task<IActionResult> GetMarketData(string category)
        {
            try
            {
                // C# menembak API lokal milik Python Service
                var response = await _httpClient.GetAsync($"http://localhost:5050/api/finance/{category}");
                
                if (!response.IsSuccessStatusCode) 
                    return StatusCode((int)response.StatusCode, "Gagal mengambil data dari Python Service");

                var content = await response.Content.ReadAsStringAsync();
                
                // Meneruskan data mentah dari Python langsung ke Electron
                return Content(content, "application/json"); 
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Python Service belum menyala: {ex.Message}");
            }
        }
    }
}