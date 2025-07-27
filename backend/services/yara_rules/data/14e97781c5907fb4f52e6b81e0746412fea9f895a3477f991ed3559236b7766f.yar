rule auto_rule_20250726233716_0890 {
  strings:
    $o0 = "dword_10022A00" wide ascii nocase
    $o1 = "dllmain_raw" wide ascii nocase
    $o2 = "__acrt_uninitialize_locks" wide ascii nocase
  condition:
    3 of ($o*)
}