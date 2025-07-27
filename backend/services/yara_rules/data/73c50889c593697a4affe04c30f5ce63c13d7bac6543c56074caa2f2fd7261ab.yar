rule auto_rule_20250726105726_2034 {
  strings:
    $o0 = "PKCS8_get_attr" wide ascii nocase
    $o1 = "EVP_MD_meth_get_init" wide ascii nocase
    $o2 = "X509v3_addr_validate_resource_set" wide ascii nocase
  condition:
    3 of ($o*)
}