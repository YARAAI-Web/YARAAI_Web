rule auto_rule_20250727005727_3305 {
  strings:
    $o0 = "dwExpectedContentTypeFlags" wide ascii nocase
    $o1 = "TrustedPublisher" wide ascii nocase
    $o2 = "__scrt_file_policy" wide ascii nocase
  condition:
    3 of ($o*)
}