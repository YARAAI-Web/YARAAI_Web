rule auto_rule_20250726100628_3918 {
  strings:
    $o0 = "lpContext" wide ascii nocase
    $o1 = "GetOpenClipboardWindow" wide ascii nocase
    $o2 = "cyDesired" wide ascii nocase
    $o3 = "nBufferSize" wide ascii nocase
  condition:
    4 of ($o*)
}