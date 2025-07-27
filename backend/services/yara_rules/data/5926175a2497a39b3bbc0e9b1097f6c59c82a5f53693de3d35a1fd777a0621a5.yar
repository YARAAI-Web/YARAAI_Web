rule auto_rule_20250726092228_1527 {
  strings:
    $o0 = "SetConsoleCursor" wide ascii nocase
    $o1 = "pSrc" wide ascii nocase
    $o2 = "GetCompressedFileSizeW" wide ascii nocase
    $o3 = "GetCompressedFileSizeA" wide ascii nocase
    $o4 = "WINNLSGetIMEHotkey" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726092231_7075 {
  strings:
    $o0 = "lpMaxMessageSize" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726092234_7573 {
  condition:
    auto_rule_20250726092228_1527 or auto_rule_20250726092231_7075
}