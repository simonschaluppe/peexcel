# Read-only collection for the editorial approval workflow.
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$hypHeaders = $null
$hypSecret = $null
try {
    $hypSecret = Get-Content -LiteralPath "$env:USERPROFILE\.hypothesis-token.dpapi" | ConvertTo-SecureString
    $hypHeaders = @{ Authorization = 'Bearer ' + [System.Net.NetworkCredential]::new('', $hypSecret).Password }
    $hypRows = [System.Collections.Generic.List[object]]::new()
    $hypOffset = 0
    do {
        $hypUrl = 'https://hypothes.is/api/search?group=Q4qRzANo&limit=200&sort=created&order=asc&offset=' + $hypOffset
        $hypPage = Invoke-RestMethod -Uri $hypUrl -Headers $hypHeaders
        foreach ($hypRow in $hypPage.rows) {
            if ($hypRow.uri -match '^https?://simonschaluppe\.github\.io/peexcel/') {
                $hypRows.Add($hypRow)
            }
        }
        $hypOffset += @($hypPage.rows).Count
    } while (@($hypPage.rows).Count -gt 0 -and $hypOffset -lt $hypPage.total)
    ConvertTo-Json -InputObject @($hypRows.ToArray()) -Depth 40
} catch {
    throw 'Hypothesis-Abruf fehlgeschlagen. Lokalen DPAPI-Token, Gruppenberechtigung und Netzwerkzugriff pruefen. Es wurden keine Annotationen veraendert.'
} finally {
    $hypHeaders = $null
    $hypSecret = $null
}
