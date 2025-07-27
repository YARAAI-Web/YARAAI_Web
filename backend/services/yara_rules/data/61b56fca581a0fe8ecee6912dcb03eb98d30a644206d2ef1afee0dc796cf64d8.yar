rule auto_rule_20250726132727_9172 {
  strings:
    $o0 = "dword_77F64" wide ascii nocase
    $o1 = "SourceString" wide ascii nocase
    $o2 = "dword_1E924" wide ascii nocase
    $o3 = "PagedPool" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}