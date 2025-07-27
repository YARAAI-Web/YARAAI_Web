rule auto_rule_20250726224554_4695 {
  strings:
    $o0 = "RegisterClipboardFormatW" wide ascii nocase
    $o1 = "FlatSB_SetScrollInfo" wide ascii nocase
    $o2 = "dxBitmap" wide ascii nocase
    $o3 = "BeginDeferWindowPos" wide ascii nocase
    $o4 = "nNumberOfCharsToWrite" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726224557_4532 {
  strings:
    $o0 = "lpaRgbValues" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726224601_8938 {
  condition:
    auto_rule_20250726224554_4695 or auto_rule_20250726224557_4532
}