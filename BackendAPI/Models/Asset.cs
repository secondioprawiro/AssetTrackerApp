namespace BackendAPI.Models;

public class Asset
{
    public int Id { get; set; }
    public string Symbol { get; set; } = string.Empty;
    public decimal Quantity { get; set; }
    public decimal BuyPrice { get; set; }
    public DateTime PurchaseDate { get; set; }
}
