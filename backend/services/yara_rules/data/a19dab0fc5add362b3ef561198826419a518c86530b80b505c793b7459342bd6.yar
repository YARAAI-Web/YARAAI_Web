rule auto_rule_20250726170953_9655 {
  strings:
    $o0 = "aMsisipDll" wide ascii nocase
  condition:
    all of them
}