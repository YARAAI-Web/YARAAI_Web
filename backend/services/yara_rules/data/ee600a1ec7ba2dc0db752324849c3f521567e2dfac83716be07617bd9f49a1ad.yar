rule auto_rule_20250726200331_6387 {
  strings:
    $o0 = "off_401004" wide ascii nocase
    $o1 = "GetOpenClipboardWindow" wide ascii nocase
    $o2 = "DdeImpersonateClient" wide ascii nocase
  condition:
    3 of ($o*)
}