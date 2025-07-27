rule auto_rule_20250726082726_6284 {
  strings:
    $o0 = "CryptUninstallCancelRetrieval" wide ascii nocase
  condition:
    all of them
}