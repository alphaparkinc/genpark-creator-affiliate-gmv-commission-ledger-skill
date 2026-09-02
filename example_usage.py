from client import CreatorAffiliateGmvCommissionLedgerClient

def main():
    client = CreatorAffiliateGmvCommissionLedgerClient()
    res = client.calculate_affiliate_payouts('crt_fashion_8812', '2026-08', 12.0)
    print('Creator Affiliate GMV Ledger: ' + res['payout_ledger_id'])
    print('Attributed GMV: $' + str(res['gross_merchandise_value_gmv_usd']) + ' (' + str(res['total_attributed_orders_count']) + ' orders)')
    print('Net Disbursable Payout: $' + str(res['net_disbursable_payout_usd']))
    print('Statement URL: ' + res['itemized_affiliate_statement_url'])

if __name__ == '__main__':
    main()
